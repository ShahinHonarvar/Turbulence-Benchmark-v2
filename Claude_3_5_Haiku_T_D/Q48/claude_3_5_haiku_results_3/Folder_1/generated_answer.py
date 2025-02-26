def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    missing_numbers = set(range(a + 1, b))
    for num in numbers[17:89]:
        if num in missing_numbers:
            missing_numbers.remove(num)
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]