def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[10]
    missing_numbers = set(range(a + 1, b)) - set(numbers[1:10])
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()