def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    s = set(t[36:53])
    result_sum = sum((x for x in range(a + 1, b) if x not in s))
    if result_sum == 0:
        return ''
    elif result_sum % 2 == 1:
        return bin(result_sum)[2:]
    else:
        return hex(result_sum)[2:]