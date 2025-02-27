def return_binary_or_hexa(int_tuple):
    a = int_tuple[13]
    b = int_tuple[91]
    sum_set = set(range(a + 1, b))
    missing = sum_set.difference(int_tuple[13:92])
    if missing:
        sum = sum(missing)
        if sum % 2:
            return bin(sum)[2:]
        else:
            return hex(sum)[2:].upper()
    else:
        return ''