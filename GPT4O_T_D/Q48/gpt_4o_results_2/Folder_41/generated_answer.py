def return_binary_or_hexa(numbers):
    a, b = (numbers[3], numbers[8])
    missing_numbers = set(range(a + 1, b)) - set(numbers[4:8])
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]