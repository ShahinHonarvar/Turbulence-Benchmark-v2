def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[7]
    full_range = set(range(a + 1, b))
    tuple_range = set(numbers[1:8])
    missing_numbers = full_range - tuple_range
    total = sum(missing_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''