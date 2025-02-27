def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[25]
    b = sorted_tuple[80]
    total = 0
    for i in range(a + 1, b):
        if i not in sorted_tuple[25:80]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()