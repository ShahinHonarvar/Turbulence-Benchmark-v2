def return_binary_or_hexa(t):
    a = t[20]
    b = t[93]
    sum_i = sum(range(a + 1, b))
    diff_sum = sum_i - sum(t[21:93])
    if diff_sum % 2:
        return bin(diff_sum)[2:]
    else:
        return hex(diff_sum)[2:]