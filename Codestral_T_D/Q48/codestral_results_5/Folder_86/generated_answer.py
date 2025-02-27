def return_binary_or_hexa(tupl):
    a = tupl[19]
    b = tupl[32]
    missing_nums = set(range(a + 1, b)) - set(tupl[19 + 1:32])
    s = sum(missing_nums)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''