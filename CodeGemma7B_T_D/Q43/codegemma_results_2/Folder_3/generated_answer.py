def find_primes_between_indices(int_list):
    prime_candidates = int_list[80:85]
    primes = []
    for candidate in prime_candidates:
        is_prime = True
        for i in range(2, candidate):
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
    return sorted(primes, reverse=True) if primes else []