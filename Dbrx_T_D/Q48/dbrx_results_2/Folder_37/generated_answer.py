def return_binary_or_hexa(t):
    a, b = (t[2], t[7])
    sum_nonpresent = sum((x for x in range(a + 1, b) if x not in t[2:7]))
    if sum_nonpresent % 2:
        return bin(sum_nonpresent)[2:]
    else:
        return hex(sum_nonpresent)[2:].upper()