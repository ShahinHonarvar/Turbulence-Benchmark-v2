def return_binary_or_hexa(test_tup):
    res = test_tup[20] + 1
    for i in range(test_tup[20] + 1, test_tup[51] - 1):
        if i not in test_tup:
            res += i
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]