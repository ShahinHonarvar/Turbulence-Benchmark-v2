def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True
    x = tup[73]
    left_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        str_n = str(n)
        if all((int(str_n[i:]) != 0 for i in range(len(str_n)))):
            if is_prime(n):
                trunc = n
                while trunc > 0:
                    if not is_prime(trunc):
                        break
                    trunc //= 10
                else:
                    left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)