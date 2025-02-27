def return_binary_or_hexa(numbers):
    a = numbers[81]
    b = numbers[86]
    potential_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[82:86])
    missing_numbers = potential_numbers - present_numbers
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]