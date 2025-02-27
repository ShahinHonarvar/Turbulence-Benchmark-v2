def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    subset = set(t[37:44])
    total_sum = sum((x for x in range(a + 1, b) if x not in subset))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()