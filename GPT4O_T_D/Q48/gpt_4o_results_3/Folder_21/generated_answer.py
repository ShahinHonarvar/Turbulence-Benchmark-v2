def return_binary_or_hexa(numbers):
    a = numbers[15]
    b = numbers[57]
    range_set = set(range(a + 1, b))
    tuple_set = set(numbers[16:57])
    missing_numbers = range_set - tuple_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]