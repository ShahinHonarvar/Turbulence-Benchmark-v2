def find_primes_between_indices(num_list):
    primes = []
    for i in range(16, 72):
        num = num_list[i]
        if num <= 1:
            continue
        is_prime = True
        for k in range(2, int(num ** 0.5) + 1):
            if num % k == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes) if primes else []