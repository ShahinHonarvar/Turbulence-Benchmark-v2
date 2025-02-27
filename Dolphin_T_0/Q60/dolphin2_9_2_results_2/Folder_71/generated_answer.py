def all_left_right_truncatable_prime(x):

    def check_truncatable(n):
        if n < 10:
            return False
        num = n
        while num >= 10:
            if not is_prime(num):
                return False
            num = num // 10
            num = num % pow(10, num.bit_length() - 1)
        return check_truncatable(num)

    def is_prime(n):
        if n < 2 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))
    primes = [i for i in range(10, x + 1) if is_prime(i) and check_truncatable(i)]
    return sorted(primes, reverse=True)