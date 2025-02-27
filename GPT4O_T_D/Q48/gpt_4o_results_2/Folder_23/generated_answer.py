def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    included_numbers = set(t[21:36])
    total_numbers = set(range(a + 1, b))
    missing_numbers = total_numbers - included_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]