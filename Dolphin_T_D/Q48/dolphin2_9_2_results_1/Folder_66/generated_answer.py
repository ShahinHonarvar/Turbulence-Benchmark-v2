def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    all_integers = list(range(a + 1, b))
    missing_integers = [i for i in all_integers if i not in t[11:77]]
    total = sum(missing_integers)
    if len(missing_integers) == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]