def return_binary_or_hexa(t):
    a = t[20]
    b = t[51]
    numbers_in_range = set(t[21:51])
    missing_numbers = set(range(a + 1, b))
    missing_sum = sum(missing_numbers - numbers_in_range)
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]