def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    full_set = set(range(a + 1, b))
    subset = set(numbers[28:96])
    missing_numbers = full_set - subset
    if missing_numbers:
        total = sum(missing_numbers)
        if total % 2 == 0:
            return format(total, 'x').lstrip('0')
        else:
            return format(total, 'b').lstrip('0')
    return ''