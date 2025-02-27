def find_primes_between_indices(int_list):
    primes = []
    for ind_num in range(16, 26):
        num = int_list[ind_num]
        if num <= 1:
            continue
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)