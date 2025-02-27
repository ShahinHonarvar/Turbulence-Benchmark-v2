def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    sublist = lst[7:10]
    primes = [x for x in sublist if is_prime(x)]
    return sorted(primes, reverse=True)