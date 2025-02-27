def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    present_numbers = set(numbers[26:80])
    all_numbers = set(range(a + 1, b))
    missing_numbers = all_numbers - present_numbers
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]