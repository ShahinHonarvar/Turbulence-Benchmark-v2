def return_binary_or_hexa(numbers):
    a = numbers[19]
    b = numbers[32]
    missing_numbers = set(range(a + 1, b))
    for num in numbers[19:33]:
        if num in missing_numbers:
            missing_numbers.remove(num)
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]