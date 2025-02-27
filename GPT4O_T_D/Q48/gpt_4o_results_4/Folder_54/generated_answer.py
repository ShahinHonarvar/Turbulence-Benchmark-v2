def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    full_range = set(range(a + 1, b))
    existing_numbers = set(t[36:64])
    missing_numbers = full_range - existing_numbers
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]