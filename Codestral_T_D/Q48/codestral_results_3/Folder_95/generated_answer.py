def return_binary_or_hexa(t):
    a = t[32]
    b = t[99]
    missing_nums = [i for i in range(a + 1, b) if i not in t[32:100]]
    s = sum(missing_nums)
    if s == 0:
        return ''
    else:
        return bin(s)[2:] if s % 2 != 0 else hex(s)[2:]