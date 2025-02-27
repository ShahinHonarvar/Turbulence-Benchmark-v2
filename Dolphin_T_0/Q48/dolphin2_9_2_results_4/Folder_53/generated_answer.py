def return_binary_or_hexa(lst):
    a = lst[200]
    b = lst[202]
    missing = [i for i in range(a + 1, b) if i not in lst[200:203]]
    if missing:
        s = sum(missing)
        return bin(s)[2:] if s % 2 != 0 else hex(s)[2:]
    else:
        return ''