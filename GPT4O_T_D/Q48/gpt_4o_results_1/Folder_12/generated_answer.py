def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    expected_range = set(range(a + 1, b))
    present_in_range = set(numbers[17:87])
    missing = expected_range - present_in_range
    if not missing:
        return ''
    total_sum = sum(missing)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]