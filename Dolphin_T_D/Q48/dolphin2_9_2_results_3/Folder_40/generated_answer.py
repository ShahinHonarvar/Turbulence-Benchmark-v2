def return_binary_or_hexa(t):
    a = t[0]
    b = t[3]
    expected_sum = b - 1 - (a + 1) + 1
    actual_sum = sum(t[1:3])
    if expected_sum == actual_sum:
        return ''
    if expected_sum % 2 != 0:
        return bin(expected_sum)[2:]
    else:
        return hex(expected_sum)[2:].upper()