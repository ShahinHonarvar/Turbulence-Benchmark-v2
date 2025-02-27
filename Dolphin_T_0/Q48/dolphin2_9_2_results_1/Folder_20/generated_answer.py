def return_binary_or_hexa(tup):
    a, b = (tup[27], tup[96])
    if b - a > 1:
        expr = [i for i in range(a + 1, b) if i not in tup]
        if expr:
            sum_ = sum(expr)
            if sum_ % 2:
                return bin(sum_)[2:]
            else:
                return hex(sum_)[2:]
    return ''