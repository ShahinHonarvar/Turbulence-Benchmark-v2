def return_binary_or_hexa(t):
    a, b = (t[13], t[76])
    missing_ints = [x for x in range(a + 1, b) if x not in t]
    if missing_ints:
        sum_ = sum(missing_ints)
        if sum_ % 2 == 0:
            return hex(sum_)[2:].upper()
        else:
            return bin(sum_)[2:]
    else:
        return ''