def return_binary_or_hexa(tup):
    a = tup[55]
    b = tup[84]
    missing_numbers = [i for i in range(a + 1, b) if i not in tup[56:84]]
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]