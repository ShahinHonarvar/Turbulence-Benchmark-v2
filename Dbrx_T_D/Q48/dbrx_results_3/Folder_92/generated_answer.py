def return_binary_or_hexa(t):
    a, b = (t[0], t[2])
    non_present = set(range(a + 1, b)) - set(t[1:3])
    if non_present:
        summation = sum(non_present)
        if summation % 2:
            return format(summation, '08b')[-(len(bin(summation)) - 2):]
        else:
            return hex(summation)[2:].upper()
    else:
        return ''