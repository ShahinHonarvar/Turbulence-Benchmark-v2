def return_binary_or_hexa(tup):
    a = tup[48]
    b = tup[76]
    numbers_in_tuple = set(tup[49:76])
    missing_numbers_sum = sum((i for i in range(a + 1, b) if i not in numbers_in_tuple))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 != 0:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]