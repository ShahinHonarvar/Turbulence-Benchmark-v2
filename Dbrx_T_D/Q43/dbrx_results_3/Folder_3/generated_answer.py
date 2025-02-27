def find_primes_between_indices(numbers):
    if len(numbers) < 85:
        return []
    primes = []
    for num in numbers[80:85]:
        is_prime = True
        if num < 2:
            is_prime = False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)