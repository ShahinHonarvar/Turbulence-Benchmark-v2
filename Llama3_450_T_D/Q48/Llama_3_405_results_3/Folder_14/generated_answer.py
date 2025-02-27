def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    absent_numbers = [i for i in range(a + 1, b) if i not in t[2:5]]
    total = sum(absent_numbers)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]