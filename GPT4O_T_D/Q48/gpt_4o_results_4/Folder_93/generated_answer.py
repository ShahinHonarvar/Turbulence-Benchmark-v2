def return_binary_or_hexa(t: tuple):
    a = t[57]
    b = t[85]
    missing_numbers = [x for x in range(a + 1, b) if x not in t[58:86]]
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]