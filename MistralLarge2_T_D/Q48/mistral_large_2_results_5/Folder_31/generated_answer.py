def return_binary_or_hexa(t):
    a, b = (t[33], t[78])
    present = set(t[33:79])
    result_sum = sum((x for x in range(a + 1, b) if x not in present))
    if result_sum == 0:
        return ''
    if result_sum % 2 == 1:
        return bin(result_sum)[2:]
    else:
        return hex(result_sum)[2:]