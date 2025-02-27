def return_binary_or_hexa(t):
    a, b = (t[44], t[91])
    present = set(t[44:92])
    result_sum = sum((x for x in range(a + 1, b) if x not in present))
    if not result_sum:
        return ''
    if result_sum % 2 == 1:
        return bin(result_sum)[2:]
    else:
        return hex(result_sum)[2:]