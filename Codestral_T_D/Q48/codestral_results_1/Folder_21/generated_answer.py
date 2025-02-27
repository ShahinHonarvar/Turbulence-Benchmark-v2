def return_binary_or_hexa(numbers):
    a = numbers[15]
    b = numbers[57]
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[16:57])
    missing_sum = sum(missing_numbers - present_numbers)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    else:
        return ''