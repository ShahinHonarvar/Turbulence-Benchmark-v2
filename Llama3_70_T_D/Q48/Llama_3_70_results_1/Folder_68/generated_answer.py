def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[9]
    full_range = set(range(a + 1, b))
    missing_numbers = full_range - set(numbers[1:9])
    missing_sum = sum(missing_numbers)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]