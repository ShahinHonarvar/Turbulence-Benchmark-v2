def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    missing_sum = 0
    missing_numbers = set(range(a + 1, b)) - set(numbers[450:906])
    if missing_numbers:
        missing_sum = sum(missing_numbers)
        if missing_sum % 2 == 1:
            return bin(missing_sum)[2:]
        else:
            return hex(missing_sum)[2:].upper()
    return ''