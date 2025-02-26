def return_binary_or_hexa(tuple_input):
    a = tuple_input[2]
    b = tuple_input[8]
    excluded_nums = set(tuple_input[2:9])
    sum_range = sum((num for num in range(a + 1, b) if num not in excluded_nums))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:].rstrip('L')