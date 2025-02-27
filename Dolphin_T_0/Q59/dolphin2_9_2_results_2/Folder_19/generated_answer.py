def all_left_truncatable_prime(x_tuple):
    x = x_tuple[67]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        while len(str_n) != 1:
            if str_n[0] == '0' or not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    left_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and is_truncatable(i):
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes