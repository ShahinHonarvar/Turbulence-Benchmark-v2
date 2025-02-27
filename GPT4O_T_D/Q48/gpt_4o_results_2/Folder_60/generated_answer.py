def return_binary_or_hexa(t):
    a = t[38]
    b = t[52]
    missing_numbers_sum = sum((x for x in range(a + 1, b) if x not in t[39:52]))
    if missing_numbers_sum == 0:
        return ''
    elif missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]