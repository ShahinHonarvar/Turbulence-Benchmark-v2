def return_binary_or_hexa(integers):
    a = integers[60]
    b = integers[90]
    missing_sum = sum((x for x in range(a + 1, b) if x not in integers[61:90]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]