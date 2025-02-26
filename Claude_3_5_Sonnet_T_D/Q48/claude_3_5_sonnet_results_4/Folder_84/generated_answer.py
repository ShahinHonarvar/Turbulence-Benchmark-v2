def return_binary_or_hexa(tuple_input):
    a = tuple_input[32]
    b = tuple_input[44]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tuple_input[32:45])
    diff_sum = sum(sum_range - sum_tuple)
    if diff_sum == 0:
        return ''
    elif diff_sum % 2 != 0:
        return bin(diff_sum)[2:]
    else:
        return hex(diff_sum)[2:].rstrip('L')