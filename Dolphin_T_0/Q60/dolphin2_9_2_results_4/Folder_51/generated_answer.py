def all_left_right_truncatable_prime(num_set, x):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        while len(n_str) > 1:
            if not is_prime(int(n_str[1:-1])):
                return False
            n_str = n_str[1:-1]
        return is_prime(int(n_str))
    primes = [i for i in num_set if i <= x and is_lr_truncatable(i)]
    return list(sorted(primes))