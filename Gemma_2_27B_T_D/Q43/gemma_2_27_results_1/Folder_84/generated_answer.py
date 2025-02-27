def find_primes_between_indices(data):
    primes = []
    for i in range(830, 850):
        n = data[i]
        if n > 1:
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    break
            else:
                primes.append(n)
    return sorted(primes)