def return_binary_or_hexa(t):
    a = t[0]
    b = t[4]
    present_numbers = set(t[:5])
    required_numbers = set(range(a + 1, b))
    missing_numbers = required_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]