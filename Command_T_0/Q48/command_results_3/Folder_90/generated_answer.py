def return_binary_or_hexa(test_tup):
    res = test_tup[60] + 1
    end = test_tup[90] - 1
    if res <= end:
        return ''
    res += end - res
    if res % 2 == 1:
        return bin(res)[2:]
    return hex(res)[2:]