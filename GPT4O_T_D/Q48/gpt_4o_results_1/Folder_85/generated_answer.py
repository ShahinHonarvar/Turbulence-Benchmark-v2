def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[8]
    all_numbers = set(range(a + 1, b))
    missing_numbers = all_numbers - set(numbers[2:8])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]