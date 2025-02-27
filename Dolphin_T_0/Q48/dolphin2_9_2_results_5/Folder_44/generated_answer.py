def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    missing = [i for i in range(a + 1, b) if i not in t[37:51]]
    result_sum = sum(missing)
    if result_sum == 0:
        return ''
    elif result_sum % 2 == 0:
        return hex(result_sum)[2:]
    else:
        return bin(result_sum)[2:]