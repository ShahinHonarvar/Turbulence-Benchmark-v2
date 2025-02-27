def return_binary_or_hexa(num_tuple):
    a = num_tuple[70]
    b = num_tuple[98]
    total = sum((i for i in range(a + 1, b) if i not in num_tuple[70:99]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]