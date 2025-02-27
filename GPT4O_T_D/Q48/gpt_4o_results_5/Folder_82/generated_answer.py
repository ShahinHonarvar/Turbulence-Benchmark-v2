def return_binary_or_hexa(numbers):
    a, b = (numbers[20], numbers[200])
    missing_sum = 0
    expected_set = set(range(a + 1, b))
    present_set = set(numbers[21:200])
    missing_set = expected_set - present_set
    missing_sum = sum(missing_set)
    if not missing_set:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]