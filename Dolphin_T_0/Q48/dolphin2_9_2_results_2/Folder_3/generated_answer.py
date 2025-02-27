def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in t:
            missing_numbers.append(i)
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]