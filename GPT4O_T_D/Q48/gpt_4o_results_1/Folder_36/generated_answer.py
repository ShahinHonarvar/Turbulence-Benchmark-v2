def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    full_range = set(range(a + 1, b))
    tuple_range = set(numbers[111:348])
    missing_numbers = full_range - tuple_range
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]