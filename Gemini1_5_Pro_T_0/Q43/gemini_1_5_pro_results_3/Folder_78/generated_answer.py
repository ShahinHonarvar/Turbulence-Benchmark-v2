def find_primes_between_indices(numbers):
    primes = []
    for i in range(29, 98):
        if i > 1:
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(numbers[i])
    primes.sort(reverse=True)
    return primes