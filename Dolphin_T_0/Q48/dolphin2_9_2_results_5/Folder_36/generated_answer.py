def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    not_in_tuple = [x for x in range(a + 1, b) if x not in t[110:348 + 1]]
    if len(not_in_tuple) == 0:
        return ''
    else:
        sum_ = sum(not_in_tuple)
        if sum_ % 2 != 0:
            return bin(sum_)[2:]
        else:
            return hex(sum_)[2:]