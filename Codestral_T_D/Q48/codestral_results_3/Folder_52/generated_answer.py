def return_binary_or_hexa(t):
    a = t[38]
    b = t[81]
    missed_nums = set(range(a + 1, b)) - set(t[38:81])
    s = sum(missed_nums)
    return bin(s)[2:] if s % 2 else hex(s)[2:]