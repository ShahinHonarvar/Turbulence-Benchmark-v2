def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(t[1:8])
    sum_result = sum(sum_range - sum_tuple)
    if sum_result == 0:
        return ''
    elif sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]