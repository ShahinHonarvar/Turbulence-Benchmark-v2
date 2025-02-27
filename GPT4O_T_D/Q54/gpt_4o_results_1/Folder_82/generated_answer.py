def all_right_truncatable_prime(integers):

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = integers[69] if len(integers) > 69 else 0
    if x <= 0:
        return []
    right_truncatable_primes = []
    for number in range(2, x):
        if is_right_truncatable_prime(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)