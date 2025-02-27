def return_binary_or_hexa(t):
    a = t[86]
    b = t[99]
    missing_numbers = set(range(a + 1, b)) - set(t[87:99])
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]