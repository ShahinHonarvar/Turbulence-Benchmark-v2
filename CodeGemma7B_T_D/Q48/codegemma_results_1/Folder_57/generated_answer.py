def return_binary_or_hexa(integers):
    a, b = (integers[25], integers[80])
    s = 0
    for i in range(a + 1, b):
        if i not in integers[25:81]:
            s += i
    return str(bin(s))[2:] if s % 2 else str(hex(s))[2:].upper()