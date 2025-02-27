def return_binary_or_hexa(lst):
    a = lst[50]
    b = lst[200]
    missing = [i for i in range(a + 1, b) if i not in lst[50:200]]
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]