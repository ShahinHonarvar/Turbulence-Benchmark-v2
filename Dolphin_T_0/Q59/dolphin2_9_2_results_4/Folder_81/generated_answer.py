def all_left_truncatable_prime(x):

    def is_left_truncatable_prime(n):
        is_n_prime = True
        temp = n
        while temp != 0:
            if not is_prime(temp):
                is_n_prime = False
                break
            temp //= 10
        return is_n_prime

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for n in range(2, x):
        if is_left_truncatable_prime(n):
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)