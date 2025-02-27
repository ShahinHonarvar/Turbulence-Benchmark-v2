def find_primes_between_indices(numbers):
    primes = []
    for n in numbers[5:8]:
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                primes.append(n)
    primes.sort(reverse=True)
    return primes