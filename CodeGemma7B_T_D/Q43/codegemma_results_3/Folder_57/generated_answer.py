def find_primes_between_indices(num_list):
    primes = []
    for num in num_list[35:89 + 1]:
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True) if primes else []