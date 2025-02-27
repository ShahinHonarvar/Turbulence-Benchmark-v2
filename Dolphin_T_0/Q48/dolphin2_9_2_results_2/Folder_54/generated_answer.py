def return_binary_or_hexa(lst):
    a = lst[35]
    b = lst[64]
    for i in range(35, 65):
        if not a + 1 <= lst[i] <= b - 1:
            lst.append(lst[i])
    missing = [i for i in range(a + 1, b) if i not in lst[35:65]]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]