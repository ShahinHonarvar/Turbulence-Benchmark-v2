def return_binary_or_hexa(numbers):
    if len(numbers) <= 35:
        return ''
    a = numbers[20]
    b = numbers[35]
    expected = set(range(a + 1, b))
    actual = set(numbers[21:35])
    missing = expected - actual
    if not missing:
        return ''
    total_sum = sum(missing)
    return bin(total_sum)[2:] if total_sum % 2 == 1 else hex(total_sum)[2:]