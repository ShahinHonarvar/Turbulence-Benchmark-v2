def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    numbers = list(range(a + 1, b))
    missing = [n for n in numbers if n not in t]
    if len(missing) == 0:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]