def return_binary_or_hexa(lst):
    a = lst[38]
    b = lst[52]
    if a + 2 > b or all((x in lst[38:53] for x in range(a + 1, b))):
        return ''
    s = sum((x for x in range(a + 1, b) if x not in lst[38:53]))
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:]