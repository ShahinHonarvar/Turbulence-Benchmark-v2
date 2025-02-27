def all_left_right_truncatable_prime(x_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = x_tuple[86]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                for i in range(len(num_str) - 1):
                    left_trunc = int(num_str[i + 1:])
                    right_trunc = int(num_str[:i + 1])
                    if is_prime(left_trunc) and is_prime(right_trunc):
                        primes.append(num)
    return primes