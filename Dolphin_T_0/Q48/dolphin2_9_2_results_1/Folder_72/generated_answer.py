def return_binary_or_hexa(lst):
    a = lst[13]
    b = lst[70]
    missing = [x for x in range(a + 1, b) if x not in lst[13:70]]
    if missing:
        s = sum(missing)
        if s % 2 == 1:
            return bin(s)[2:]
        else:
            return hex(s)[2:].upper()
    else:
        return ''