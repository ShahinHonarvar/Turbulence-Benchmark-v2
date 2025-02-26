def return_binary_or_hexa(tuple_input):
    a = tuple_input[35]
    b = tuple_input[64]
    sum_range = set(range(a + 1, b))
    tuple_range = set(tuple_input[35:65])
    missing_sum = sum(sum_range - tuple_range)
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]