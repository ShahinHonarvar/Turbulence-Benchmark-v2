def find_primes_between_indices(data):
    primes = []
    for i in range(13, 69):
        if i < len(data) and data[i] > 1:
            is_prime = True
            for j in range(2, int(data[i] ** 0.5) + 1):
                if data[i] % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(data[i])
    primes.sort()
    return primes