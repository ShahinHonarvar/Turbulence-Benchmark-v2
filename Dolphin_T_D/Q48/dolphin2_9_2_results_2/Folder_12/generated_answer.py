def return_binary_or_hexa(t):
    a = t[16]
    b = t[87]
    missing = [num for num in range(a + 1, b) if num ** 2 not in t]
    if missing:
        sum_ = sum(missing)
        if sum_ % 2:
            return bin(sum_)[2:]
        else:
            return hex(sum_)[2:]
    return ''