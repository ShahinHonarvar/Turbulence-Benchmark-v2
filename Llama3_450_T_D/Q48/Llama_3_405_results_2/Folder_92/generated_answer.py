def return_binary_or_hexa(numbers):
    a, _, b = numbers
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((num for num in numbers[1:-1] if a < num < b))
    missing_sum = expected_sum - actual_sum
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]