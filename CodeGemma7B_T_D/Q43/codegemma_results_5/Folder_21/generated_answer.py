def find_primes_between_indices(lst):
    primes = []
    for idx in range(478, 950):
        num = lst[idx]
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes if primes else []