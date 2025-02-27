def return_binary_or_hexa(t):
    a = t[60]
    b = t[90]
    missing_numbers = {i for i in range(a + 1, b)} - set(t[60:91])
    s = sum(missing_numbers)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''