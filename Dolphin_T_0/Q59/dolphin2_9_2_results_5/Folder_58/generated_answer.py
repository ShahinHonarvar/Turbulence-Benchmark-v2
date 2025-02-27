def all_left_truncatable_prime(arg):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = arg[975]
    left_truncatable_primes = []
    for num in range(x - 1, 0, -1):
        trunc = num
        while trunc:
            if not is_prime(trunc):
                break
            trunc //= 10
        else:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)