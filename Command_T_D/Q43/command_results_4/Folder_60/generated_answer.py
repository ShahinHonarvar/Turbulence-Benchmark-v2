def find_primes_between_indices(lst):
    lst = lst[46:85]
    prime_list = []
    for n in lst:
        if all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))):
            prime_list.append(n)
    return prime_list