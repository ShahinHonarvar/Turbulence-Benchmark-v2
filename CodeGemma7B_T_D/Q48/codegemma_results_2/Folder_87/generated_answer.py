def return_binary_or_hexa(t):
    a, b = (t[20], t[43])
    sum = 0
    for k in range(a + 1, b):
        if k not in t[20:44]:
            sum += k
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()