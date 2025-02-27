def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    range_set = set(range(a + 1, b))
    tuple_set = set(numbers[11:76])
    missing_numbers = range_set - tuple_set
    total = sum(missing_numbers)
    if total == 0:
        return ''
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]