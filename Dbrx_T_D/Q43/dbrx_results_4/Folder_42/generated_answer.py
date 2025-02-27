def find_primes_between_indices(numbers):
    prime_indices = list(range(30, 44))
    primes = []
    for index in prime_indices:
        if index < 0 or index >= len(numbers):
            continue
        is_prime = True
        for i in range(2, numbers[index]):
            if numbers[index] % i == 0:
                is_prime = False
                break
        if is_prime and numbers[index] > 1:
            primes.append(numbers[index])
    return sorted(primes)