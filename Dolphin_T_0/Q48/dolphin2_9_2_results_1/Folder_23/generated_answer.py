def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    present = set(t[21:36])
    missing = [i for i in range(a + 1, b) if i not in present]
    sum_of_missing = sum(missing)
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]