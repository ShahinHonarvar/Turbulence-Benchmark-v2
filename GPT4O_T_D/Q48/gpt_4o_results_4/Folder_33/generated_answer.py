def return_binary_or_hexa(integers):
    if len(integers) <= 35:
        return ''
    a = integers[13]
    b = integers[35]
    full_range = set(range(a + 1, b))
    present_numbers = set(integers[14:35])
    missing_numbers = full_range - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]