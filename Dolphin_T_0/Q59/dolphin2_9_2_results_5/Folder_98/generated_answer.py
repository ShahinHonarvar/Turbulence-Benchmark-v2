def all_left_truncatable_prime(t):

    def is_truncatable(n):
        n_list = list(map(int, str(n)))
        while n_list:
            n = int(''.join(map(str, n_list)))
            if n < 2 or n % 2 == 0:
                return False
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            n_list = n_list[1:]
        return True
    x = t[8]
    primes = [i for i in range(x, 1, -1) if is_truncatable(i)]
    return primes