def find_primes_between_indices(lst):

    def check_prime_number(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([x for x in lst[59:98] if check_prime_number(x)], reverse=True)