def return_binary_or_hexa(test_tup):
    res = test_tup[48] + 1
    res += test_tup[49] - 1
    res += test_tup[50] - 1
    res += test_tup[51] - 1
    res += test_tup[52] - 1
    res += test_tup[53] - 1
    res += test_tup[54] - 1
    res += test_tup[55] - 1
    res += test_tup[56] - 1
    res += test_tup[57] - 1
    res += test_tup[58] - 1
    res += test_tup[59] - 1
    res += test_tup[60] - 1
    res += test_tup[61] - 1
    res += test_tup[62] - 1
    res += test_tup[63] - 1
    res += test_tup[64] - 1
    res += test_tup[65] - 1
    res += test_tup[66] - 1
    res += test_tup[67] - 1
    res += test_tup[68] - 1
    res += test_tup[69] - 1
    res += test_tup[70] - 1
    res += test_tup[71] - 1
    res += test_tup[72] - 1
    res += test_tup[73] - 1
    res += test_tup[74] - 1
    res += test_tup[75] - 1
    res += test_tup[76] - 1
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)