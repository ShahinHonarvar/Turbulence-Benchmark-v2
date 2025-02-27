def return_binary_or_hexa(numbers):
    a = numbers[29]
    b = numbers[53]
    numbers_in_range = set(numbers[30:54])
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers_in_range]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]