def return_binary_or_hexa(t):
    a, b = (t[62], t[96])
    sum = 0
    for n in range(a + 1, b):
        if n not in t[62:97]:
            sum += n
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()