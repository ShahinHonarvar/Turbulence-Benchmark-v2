def return_binary_or_hexa(test_tup):
    res = test_tup[22] + 1
    end = test_tup[24] - 1
    if res <= end:
        res += test_tup[23] - test_tup[22]
        if res % 2 == 1:
            return bin(res)[2:]
        else:
            return hex(res)[2:]
    else:
        return ''