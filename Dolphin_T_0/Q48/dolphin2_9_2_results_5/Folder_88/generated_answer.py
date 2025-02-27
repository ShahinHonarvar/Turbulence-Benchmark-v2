def return_binary_or_hexa(t):
    a = t[3]
    b = t[9]
    is_all_present = all((i in t[3:10] for i in range(a + 1, b)))
    if is_all_present:
        return ''
    else:
        sum_of = sum((i for i in range(a + 1, b) if i not in t[3:10]))
        if sum_of % 2 != 0:
            return bin(sum_of)[2:]
        else:
            return hex(sum_of)[2:]