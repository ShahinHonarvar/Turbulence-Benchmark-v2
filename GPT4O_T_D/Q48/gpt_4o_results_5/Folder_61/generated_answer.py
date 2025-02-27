def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[8]
    all_numbers = set(range(a + 1, b))
    missing_numbers = all_numbers - set(numbers[1:9])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]