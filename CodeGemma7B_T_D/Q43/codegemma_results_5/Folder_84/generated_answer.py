def find_primes_between_indices(int_list):
    primes = []
    for i in range(830, 850):
        n = int_list[i]
        if n <= 1:
            continue
        is_prime = True
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return sorted(primes) or []