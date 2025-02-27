def return_binary_or_hexa(numbers):
    if len(numbers) < 85:
        return ''
    a = numbers[77]
    b = numbers[84]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((x for x in range(a + 1, b) if x not in numbers[78:84]))
    missing_sum = expected_sum - actual_sum
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]