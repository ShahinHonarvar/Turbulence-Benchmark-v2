def return_binary_or_hexa(t):
    a = t[36]
    b = t[85]
    numbers = list(range(a + 1, b))
    missing_numbers = [n for n in numbers if n not in t[36:86]]
    total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]