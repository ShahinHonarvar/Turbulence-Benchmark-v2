def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    missing_numbers = set(range(a + 1, b)) - set(numbers[7:9])
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]