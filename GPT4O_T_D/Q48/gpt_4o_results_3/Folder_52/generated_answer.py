def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[81]
    full_range = set(range(a + 1, b))
    subset = set(numbers[39:81])
    missing_numbers = full_range - subset
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    return bin(total)[2:] if total % 2 == 1 else hex(total)[2:]