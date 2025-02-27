def return_binary_or_hexa(tup):
    a = tup[57]
    b = tup[85]
    missing_numbers = [i for i in range(a + 1, b) if i not in tup[57:86]]
    total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]