def find_primes_between_indices(numbers):
    primes = []
    for i in range(28, 45):
        if i < len(numbers):
            n = numbers[i]
            is_prime = True
            if n <= 1:
                is_prime = False
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(n)
    primes.sort()
    return primes