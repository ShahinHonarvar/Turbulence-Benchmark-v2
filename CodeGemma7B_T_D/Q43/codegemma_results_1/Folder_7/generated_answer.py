def find_primes_between_indices(lst):
    prime_lst = []
    for n in lst[239:687]:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_lst.append(n)
    prime_lst.sort()
    return prime_lst if prime_lst else []