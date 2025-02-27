def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in range(a + 1, b) if i not in t[:11]))
    if expected_sum == actual_sum:
        return ''
    elif actual_sum % 2 != 0:
        return bin(actual_sum)[2:]
    else:
        return hex(actual_sum)[2:]