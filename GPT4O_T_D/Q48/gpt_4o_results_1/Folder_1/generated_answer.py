def return_binary_or_hexa(numbers):
    if len(numbers) < 89:
        return ''
    a, b = (numbers[17], numbers[88])
    full_set = set(range(a + 1, b))
    tuple_set = set(numbers[18:88])
    missing_set = full_set - tuple_set
    if not missing_set:
        return ''
    total_sum = sum(missing_set)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]