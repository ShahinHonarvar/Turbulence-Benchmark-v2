def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    items = [i for i in range(a + 1, b) if i not in t]
    suma = sum(items)
    if suma % 2 == 0:
        return hex(suma)[2:]
    else:
        return bin(suma)[2:]