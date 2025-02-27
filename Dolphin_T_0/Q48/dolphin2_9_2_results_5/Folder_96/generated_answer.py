def return_binary_or_hexa(t):
    a = t[50]
    b = t[200]
    missing = [x for x in range(a + 1, b) if x not in t]
    result_sum = sum(missing)
    if result_sum % 2 == 0:
        return hex(result_sum)[2:]
    else:
        return bin(result_sum)[2:]