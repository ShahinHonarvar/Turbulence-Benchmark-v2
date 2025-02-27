def return_binary_or_hexa(t):
    a, b = (t[51], t[76])
    missing_numbers = set(range(a + 1, b)) - set(t[51 + 1:76])
    total = sum(missing_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]