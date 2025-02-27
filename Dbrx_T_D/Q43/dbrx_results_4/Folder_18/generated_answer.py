def find_primes_between_indices(numbers):
    primes = []
    for i in range(430, 806):
        if i < 0 or i >= len(numbers):
            continue
        is_prime = True
        num = abs(numbers[i])
        if num < 2:
            continue
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort()
    return primes