def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[90]
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[56 + 1:90])
    missing_sum = sum(missing_numbers - present_numbers)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]