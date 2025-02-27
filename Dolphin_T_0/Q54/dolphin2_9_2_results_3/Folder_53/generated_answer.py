def all_right_truncatable_prime(T):
    x = T[86]
    prime = []
    i = 2
    while T[0] < x:
        if is_prime(T[0]):
            if es_truncable(T[0]):
                prime.append(T[0])
        i += 1
    prime.sort(reverse=True)
    if len(prime) == 0:
        return []
    else:
        return prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def es_truncable(num):
    cadena = str(num)
    for i in range(len(cadena) - 1):
        if not is_prime(int(cadena[i:])):
            return False
    return True