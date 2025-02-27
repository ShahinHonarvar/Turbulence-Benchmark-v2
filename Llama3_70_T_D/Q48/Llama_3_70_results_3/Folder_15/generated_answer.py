def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[4]
    full_range = set(range(a + 1, b))
    partial_range = set(numbers[1:4])
    missing_numbers = full_range - partial_range
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]