def return_binary_or_hexa(t):
    a = t[19]
    b = t[32]
    missing_nums = set(range(a + 1, b)) - set(t[19 + 1:32])
    missing_sum = sum(missing_nums)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]