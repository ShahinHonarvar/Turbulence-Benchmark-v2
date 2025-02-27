def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    num_set = set(t[21:36])
    total_sum = sum((x for x in range(a + 1, b) if x not in num_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]