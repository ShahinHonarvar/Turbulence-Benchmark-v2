def find_primes_between_indices(numbers):
    primes = []
    for i in range(28, 37):
        n = numbers[i]
        if n > 1:
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    break
            else:
                primes.append(n)
    primes.sort()
    return primes