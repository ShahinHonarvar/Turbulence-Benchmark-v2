def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    present_integers = set(t[1:10])
    missing_integers = [i for i in range(a + 1, b) if i not in present_integers]
    if sum(missing_integers) % 2 == 0:
        return hex(sum(missing_integers))[2:]
    else:
        return bin(sum(missing_integers))[2:]