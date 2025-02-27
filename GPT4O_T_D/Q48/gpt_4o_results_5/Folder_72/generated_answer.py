def return_binary_or_hexa(numbers):
    if len(numbers) < 71:
        return ''
    a = numbers[13]
    b = numbers[70]
    range_set = set(range(a + 1, b))
    tuple_set = set(numbers[14:70])
    missing_numbers = range_set - tuple_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]