def return_binary_or_hexa(tup):
    a = tup[49]
    b = tup[74]
    all_ints = set(range(a + 1, b))
    tup_ints = set(tup)
    sum = 0
    for i in all_ints:
        if i not in tup_ints:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()