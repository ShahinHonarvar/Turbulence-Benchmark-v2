def return_binary_or_hexa(lst):
    a = lst[46]
    b = lst[91]
    missing = [i for i in range(a + 1, b) if i not in lst[46:91]]
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]