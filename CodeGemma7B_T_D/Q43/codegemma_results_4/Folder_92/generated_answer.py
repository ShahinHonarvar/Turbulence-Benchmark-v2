def find_primes_between_indices(prime_list):
    primes = prime_list[7:9]
    return sorted(primes) if any((prime for prime in primes if prime.isnumeric())) else []