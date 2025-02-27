def all_left_right_truncatable_prime(x_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if str(n).count('0') > 0:
            return False
        while n > 9:
            if not is_prime(int(str(n)[1:-1])):
                return False
            n = int(str(n)[1:-1])
        return True
    x = x_tuple[87]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_primes = [i for i in primes if is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes)