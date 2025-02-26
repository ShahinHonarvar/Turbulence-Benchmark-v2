def return_binary_or_hexa(t):
    a = t[46]
    b = t[91]
    missing_numbers = [x for x in range(a + 1, b) if x not in t[46:92]]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]