def return_binary_or_hexa(seq):
    a, b = (seq[933], seq[996])
    tot = 0
    for i in range(a + 1, b):
        if i not in seq[933:997]:
            tot += i
    if tot % 2:
        return bin(tot)[2:]
    else:
        return hex(tot)[2:].upper()