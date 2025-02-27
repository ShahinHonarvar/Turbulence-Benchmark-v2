def find_primes_between_indices(list_of_integers):
    primes = []
    for number in list_of_integers[261:460]:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return sorted(primes) or []