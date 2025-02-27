def return_binary_or_hexa(numbers):
    if len(numbers) < 88 or numbers[16] == numbers[87] - 1:
        return ''
    a = numbers[16]
    b = numbers[87]
    range_set = set(range(a + 1, b))
    tuple_set = set(numbers[17:87])
    missing_numbers = range_set - tuple_set
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]