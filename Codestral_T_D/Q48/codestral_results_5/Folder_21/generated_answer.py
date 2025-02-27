def return_binary_or_hexa(t):
    a = t[15]
    b = t[57]
    missing_numbers = [i for i in range(a + 1, b) if i not in t[15:57]]
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''