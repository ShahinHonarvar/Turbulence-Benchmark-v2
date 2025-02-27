def all_left_right_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
                return False
        return True
    x = args[1]
    primes = [i for i in range(2, x + 1) if is_prime(i) and left_right_truncatable(i)]
    return sorted(primes, reverse=True)