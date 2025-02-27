def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[87:99])
    missing_sum = sum(missing_numbers - present_numbers)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]