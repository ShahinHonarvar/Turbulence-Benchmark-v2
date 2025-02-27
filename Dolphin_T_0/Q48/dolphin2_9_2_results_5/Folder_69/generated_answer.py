def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    missing = [i for i in range(a + 1, b) if i not in t[40:43]]
    sum_ = sum(missing) if missing else 0
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()