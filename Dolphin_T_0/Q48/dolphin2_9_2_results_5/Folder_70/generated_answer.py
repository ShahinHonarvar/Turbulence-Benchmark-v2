def return_binary_or_hexa(my_tuple):
    a = my_tuple[43]
    b = my_tuple[70]
    range_sum = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in my_tuple[44:70]]
    if missing:
        total = sum(missing)
        if total % 2 == 1:
            return bin(total)[2:]
        else:
            return hex(total)[2:].upper()
    else:
        return ''