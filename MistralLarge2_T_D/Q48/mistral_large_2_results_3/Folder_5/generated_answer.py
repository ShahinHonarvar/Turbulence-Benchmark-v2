def return_binary_or_hexa(t):
    a = t[2]
    b = t[8]
    range_sum = sum((x for x in range(a + 1, b) if x not in t[2:9]))
    if range_sum == 0:
        return ''
    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:].upper()