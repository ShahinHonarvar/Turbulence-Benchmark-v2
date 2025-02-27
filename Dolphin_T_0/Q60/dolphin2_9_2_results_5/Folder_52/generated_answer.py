def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def is_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if is_prime(int(num_str[i:])) and is_prime(int(num_str[:i + 1])):
                continue
            else:
                return False
        return True
    x = num_tuple[52]
    truncatable_primes = [i for i in range(x, 1, -1) if is_prime(i) and is_truncatable(i)]
    return truncatable_primes