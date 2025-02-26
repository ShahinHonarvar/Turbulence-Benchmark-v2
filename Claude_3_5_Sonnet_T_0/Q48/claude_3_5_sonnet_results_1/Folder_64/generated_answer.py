def return_binary_or_hexa(t):
    a, b = (t[0], t[5])
    sum_range = set(range(a + 1, b))
    sum_tuple = set(t[1:5])
    total_sum = sum(sum_range - sum_tuple)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]