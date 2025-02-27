def return_binary_or_hexa(numbers):
    a, b = (numbers[32], numbers[44])
    if a + 1 >= b - 1:
        return ''
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[32:45])
    missing_numbers -= present_numbers
    total = sum(missing_numbers)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]