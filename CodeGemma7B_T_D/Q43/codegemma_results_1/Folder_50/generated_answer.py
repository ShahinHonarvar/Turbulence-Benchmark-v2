def find_primes_between_indices(num_list):
    primes = [n for n in num_list[23:60] if all((n % i != 0 for i in range(2, n)))]
    primes.sort(reverse=True)
    return primes if primes else []