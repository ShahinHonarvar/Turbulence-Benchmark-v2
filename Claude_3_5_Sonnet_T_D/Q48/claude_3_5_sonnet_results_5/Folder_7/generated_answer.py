def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[97]
    excluded_numbers = set(tuple_input[10:98])
    sum_range = sum((num for num in range(a + 1, b) if num not in excluded_numbers))
    if sum_range == 0:
        return ''
    if sum_range % 2 != 0:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]