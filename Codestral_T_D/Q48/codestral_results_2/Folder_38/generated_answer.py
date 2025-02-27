def return_binary_or_hexa(t):
    a = t[36]
    b = t[85]
    missing_numbers = [i for i in range(a + 1, b) if i not in t[36:86]]
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]