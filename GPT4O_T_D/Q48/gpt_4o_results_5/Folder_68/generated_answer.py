def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[9]
    full_range_sum = sum(range(a + 1, b))
    present_sum = sum((num for num in numbers[1:10] if a < num < b))
    missing_sum = full_range_sum - present_sum
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]