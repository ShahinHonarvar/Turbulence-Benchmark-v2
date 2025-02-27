def return_binary_or_hexa(t):
    a = t[44]
    b = t[91]
    present = [i for i in t if a < i < b]
    if all((i in present for i in range(a + 1, b))):
        return ''
    else:
        missing = [i for i in range(a + 1, b) if i not in present]
        sum_missing = sum(missing)
        return bin(sum_missing)[2:] if sum_missing % 2 != 0 else hex(sum_missing)[2:]