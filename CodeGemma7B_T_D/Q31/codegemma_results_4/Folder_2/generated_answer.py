def if_perfect_num(lista):
    if lista[702] % suma_fact(lista[702]) == 0:
        return True
    else:
        return False

def suma_fact(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma