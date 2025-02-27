def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    missing_numbers = set(range(a + 1, b))
    existing_numbers = set(numbers[57 + 1:85])
    missing_sum = sum(missing_numbers - existing_numbers)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]