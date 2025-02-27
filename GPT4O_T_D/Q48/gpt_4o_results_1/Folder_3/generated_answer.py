def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[88]
    full_range = set(range(a + 1, b))
    existing = set(numbers[57:88])
    missing = full_range - existing
    if not missing:
        return ''
    total_sum = sum(missing)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]