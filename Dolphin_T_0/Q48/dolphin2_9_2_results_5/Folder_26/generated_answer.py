def return_binary_or_hexa(int_tuple):
    if len(int_tuple) < 100:
        a = int_tuple[68]
        b = int_tuple[99]
        not_in_tuple = set(range(a + 1, b)) - set(int_tuple[68:100])
        total = sum(not_in_tuple)
        if total % 2 != 0:
            return bin(total)[2:]
        else:
            return hex(total)[2:]
    else:
        return ''