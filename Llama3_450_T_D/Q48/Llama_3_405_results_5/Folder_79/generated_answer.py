def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    absent_numbers = [i for i in range(a + 1, b) if i not in t[1:7]]
    total = sum(absent_numbers)
    if not absent_numbers:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]