def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[4]
    to_sum = set(range(a + 1, b))
    present_numbers = set(numbers[1:5])
    missing_numbers = to_sum - present_numbers
    sum_result = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]