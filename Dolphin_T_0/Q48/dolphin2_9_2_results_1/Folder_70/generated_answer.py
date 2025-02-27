def return_binary_or_hexa(lst):
    a = lst[43]
    b = lst[70]
    missing = [i for i in range(a + 1, b) if i not in lst[43:70 + 1]]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]