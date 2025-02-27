def return_binary_or_hexa(lst):
    a = lst[46]
    b = lst[91]
    included = set(lst[46:92])
    total = sum((x for x in range(a + 1, b) if x not in included))
    if total % 2 == 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()