def return_binary_or_hexa(t):
    a, b = (t[6], t[9])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[6:10]:
            sum += i
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()