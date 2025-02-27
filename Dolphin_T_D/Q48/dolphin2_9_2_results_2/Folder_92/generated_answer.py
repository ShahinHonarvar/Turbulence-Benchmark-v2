def return_binary_or_hexa(t):
    a = t[0]
    b = t[2]
    sum_integers = sum((i for i in range(a + 1, b) if i not in t))
    if len(range(a + 1, b)) == len(t[1:]):
        return ''
    else:
        return bin(sum_integers)[2:] if sum_integers % 2 != 0 else hex(sum_integers)[2:]