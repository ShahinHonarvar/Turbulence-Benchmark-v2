def return_binary_or_hexa(numbers):
    a = numbers[7]
    b = numbers[9]
    range_set = set(range(a + 1, b))
    tuple_set = set(numbers[8:9])
    missing_numbers = range_set - tuple_set
    total_sum = sum(missing_numbers)
    if missing_numbers:
        if total_sum % 2 == 0:
            return hex(total_sum)[2:]
        else:
            return bin(total_sum)[2:]
    return ''