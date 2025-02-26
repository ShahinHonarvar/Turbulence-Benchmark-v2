def return_binary_or_hexa(tuple_input):
    a = tuple_input[86]
    b = tuple_input[89]
    missing_numbers = set(range(a + 1, b))
    for num in tuple_input[86:90]:
        if num in missing_numbers:
            missing_numbers.remove(num)
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]