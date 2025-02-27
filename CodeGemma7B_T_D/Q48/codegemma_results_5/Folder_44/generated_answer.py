def return_binary_or_hexa(tupla):
    a = tupla[36]
    b = tupla[52]
    lista = []
    suma = 0
    for i in range(a + 1, b):
        if i not in tupla[36:53]:
            lista.append(i)
            suma += i
    if suma % 2 == 0:
        return hex(suma)[2:]
    else:
        return bin(suma)[2:]