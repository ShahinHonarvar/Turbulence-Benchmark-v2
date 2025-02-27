def return_binary_or_hexa(tupl):
    a, b = (tupl[45], tupl[48])
    suma = 0
    for num in range(a + 1, b):
        if num not in tupl[45:49]:
            suma += num
    if suma % 2 == 0:
        return hex(suma)[2:]
    else:
        return bin(suma)[2:]