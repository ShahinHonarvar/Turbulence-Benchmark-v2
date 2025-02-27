def return_binary_or_hexa(t: tuple):
    a, b = (t[10], t[100])
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum(t) - sum(t[10:101])
    if expected_sum != actual_sum:
        s = str(expected_sum - actual_sum)
        if expected_sum % 2 == 0:
            return s.upper()
        else:
            return bin(int(s))[2:]
    else:
        return ''