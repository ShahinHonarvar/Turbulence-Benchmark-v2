def find_primes_between_indices(numbers):
    primes = []
    for i in range(len(numbers)):
        if numbers[i] > 1:
            is_prime = True
            for j in range(2, int(numbers[i] ** 0.5) + 1):
                if numbers[i] % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(numbers[i])
    primes = sorted(primes, reverse=True)
    if len(primes) < 472:
        return []
    return primes[0:472]