def return_binary_or_hexa(lst):
    a = lst[10]
    b = lst[97]
    s = sum(set(range(a + 1, b)) - set(lst[10:98]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]