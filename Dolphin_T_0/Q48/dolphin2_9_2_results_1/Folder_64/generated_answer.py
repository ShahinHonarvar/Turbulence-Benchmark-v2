def return_binary_or_hexa(t):
    a, b = (t[0], t[5])
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum(t)
    if expected_sum == actual_sum:
        return ''
    return '{bin}' if expected_sum % 2 else '{hex}'.format(bin=bin(expected_sum), hex=hex(expected_sum))