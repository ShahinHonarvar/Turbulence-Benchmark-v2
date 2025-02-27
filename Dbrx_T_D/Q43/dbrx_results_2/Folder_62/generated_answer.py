def find_primes_between_indices(numeros):
    primes = []
    for i in range(len(numeros)):
        if i < 29 or i > 97:
            continue
        if numeros[i] > 1:
            for j in range(2, numeros[i]):
                if numeros[i] % j == 0:
                    break
            else:
                primes.append(numeros[i])
    primes.sort(reverse=True)
    return primes