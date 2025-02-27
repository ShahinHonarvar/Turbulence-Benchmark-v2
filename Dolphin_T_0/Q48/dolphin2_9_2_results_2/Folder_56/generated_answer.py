def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    missing = []
    for num in range(a + 1, b):
        if num not in t:
            missing.append(num)
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]