def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = input_tuple[43]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in primes if is_right_truncatable(i)], key=int)