def return_binary_or_hexa(numbers):
    a = numbers[39]
    b = numbers[43]
    range_set = set(range(a + 1, b))
    tuple_subset = set(numbers[40:43])
    missing_numbers = range_set - tuple_subset
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]