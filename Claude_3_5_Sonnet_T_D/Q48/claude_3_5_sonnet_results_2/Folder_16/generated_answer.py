def return_binary_or_hexa(t):
    a = t[90]
    b = t[97]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(t[90:98])
    missing_sum = sum(sum_range - sum_tuple)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]