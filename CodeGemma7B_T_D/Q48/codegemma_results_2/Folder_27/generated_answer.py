def return_binary_or_hexa(t):
    a, b = (t[86], t[89])
    total = 0
    for i in range(a + 1, b):
        if i not in t[a + 1:89] + t[89 + 1:]:
            total += i
    return bin(total)[2:].zfill(len(str(total))) if total % 2 else hex(total)[2:].zfill(len(str(total)))