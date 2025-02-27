def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    numbers_in_tuple = set(t[2:8])
    missing_numbers_sum = sum((i for i in range(a + 1, b) if i not in numbers_in_tuple))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]