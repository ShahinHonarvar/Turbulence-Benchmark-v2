def return_binary_or_hexa(t):
    a = t[40]
    b = t[200]
    missing_numbers = [i for i in range(a + 1, b) if i not in t[41:201]]
    total = sum(missing_numbers)
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]