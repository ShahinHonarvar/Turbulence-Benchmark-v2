def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    relevant_lst = lst[45:81]
    primes = [x for x in relevant_lst if is_prime(x)]
    return sorted(primes, reverse=True) if primes else []