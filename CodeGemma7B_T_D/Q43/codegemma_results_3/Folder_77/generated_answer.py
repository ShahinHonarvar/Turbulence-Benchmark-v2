def find_primes_between_indices(int_list):
    primes = []
    for num in int_list[287:929]:
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes) if primes else []