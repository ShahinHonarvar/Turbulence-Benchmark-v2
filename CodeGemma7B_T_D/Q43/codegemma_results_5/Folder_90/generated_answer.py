def find_primes_between_indices(int_list):
    primes = []
    for i in range(413, 449):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    primes.sort()
    return primes