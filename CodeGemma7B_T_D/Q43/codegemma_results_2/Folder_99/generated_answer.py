def find_primes_between_indices(list_of_integers):
    primes = []
    for num in list_of_integers[187:272]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    primes.sort()
    return primes or []