def return_binary_or_hexa(lst):
    a = lst[3]
    b = lst[9]
    is_empty = True
    total = 0
    for i in range(a + 1, b):
        if i not in lst[4:9]:
            is_empty = False
            total += i
    if is_empty:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]