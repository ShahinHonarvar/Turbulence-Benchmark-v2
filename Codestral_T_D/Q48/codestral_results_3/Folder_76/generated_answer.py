def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    missing_nums = [i for i in range(a + 1, b) if i not in t[450:906]]
    s = sum(missing_nums)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''