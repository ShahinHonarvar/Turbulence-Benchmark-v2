def return_binary_or_hexa(numbers):
    if len(numbers) < 29:
        return ''
    a = numbers[10]
    b = numbers[28]
    expected_sum = sum(range(a + 1, b))
    present_sum = sum((x for x in numbers[11:28] if a < x < b))
    missing_sum = expected_sum - present_sum
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]