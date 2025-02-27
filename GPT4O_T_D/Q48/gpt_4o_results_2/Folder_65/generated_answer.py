def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    all_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[52:76])
    missing_numbers = all_numbers - present_numbers
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]