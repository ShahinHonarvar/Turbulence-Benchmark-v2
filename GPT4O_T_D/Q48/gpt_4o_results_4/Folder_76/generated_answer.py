def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    needed_numbers = set(range(a + 1, b))
    missing_numbers = needed_numbers - set(t[451:905])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]