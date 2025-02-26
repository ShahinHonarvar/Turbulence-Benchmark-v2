def return_binary_or_hexa(tuple_input):
    a = tuple_input[20]
    b = tuple_input[36]
    subset = set(tuple_input[20:37])
    sum_missing = sum((num for num in range(a + 1, b) if num not in subset))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]