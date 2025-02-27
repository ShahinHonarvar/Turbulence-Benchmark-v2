def return_binary_or_hexa(numbers):
    a = numbers[81]
    b = numbers[86]
    missing_numbers_sum = sum((i for i in range(a + 1, b) if i not in numbers[82:86]))
    if missing_numbers_sum == 0:
        return ''
    elif missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]