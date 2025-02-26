def return_binary_or_hexa(tuple_input):
    a = tuple_input[18]
    b = tuple_input[60]
    excluded_numbers = set(tuple_input[19:60])
    sum_total = sum((num for num in range(a + 1, b) if num not in excluded_numbers))
    if sum_total == 0:
        return ''
    if sum_total % 2 == 1:
        return bin(sum_total)[2:]
    else:
        return hex(sum_total)[2:]