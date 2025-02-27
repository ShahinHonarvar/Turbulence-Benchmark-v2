def return_binary_or_hexa(t):
    a = t[20]
    b = t[35]
    present = set(t[20:36])
    missing_nums = [i for i in range(a + 1, b) if i not in present]
    if not missing_nums:
        return ''
    s = sum(missing_nums)
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:]