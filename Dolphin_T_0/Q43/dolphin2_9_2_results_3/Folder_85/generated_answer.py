def find_primes_between_indices(lst):
    prime_lst = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(32, 36):
        if is_prime(lst[i]):
            prime_lst.append(lst[i])
    return sorted(prime_lst)