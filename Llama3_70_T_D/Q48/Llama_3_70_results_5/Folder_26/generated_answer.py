def return_binary_or_hexa(t):
    a = t[68]
    b = t[99]
    missing_numbers = [i for i in range(a + 1, b) if i not in t[68:100]]
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]