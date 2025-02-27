def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    expected = range(a + 1, b)
    actual = t[1:7]
    missing = [i for i in expected if i not in actual]
    result_sum = sum(missing)
    if result_sum % 2 != 0:
        return bin(result_sum).replace('0b', '')
    else:
        return hex(result_sum).replace('0x', '')