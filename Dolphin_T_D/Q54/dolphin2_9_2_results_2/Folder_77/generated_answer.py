def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n >= 10:
            if not is_prime(n):
                return False
            n //= 10
        return is_prime(n)
    prime_numbers = []
    for num in range(x - 1, 0, -1):
        if is_right_truncatable_prime(num):
            prime_numbers.append(num)
    return prime_numbers