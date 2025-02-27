from itertools import islice

def all_left_right_truncatable_prime(t):
    x = t[14]

    def is_left_truncatable_prime(n):
        while n > 9:
            if not (n > 10 and all((n % i for i in range(2, int(n ** 0.5) + 1)))):
                return False
            n *= 0.1
        return True

    def is_right_truncatable_prime(n):
        while n > 9:
            if not (n > 10 and all((n % i for i in range(2, int(n ** 0.5) + 1)))):
                return False
            n //= 10
        return True

    def is_left_and_right_truncatable_prime(n):
        return is_left_truncatable_prime(n) and is_right_truncatable_prime(n)
    primes = [i for i in range(2, int(x ** 0.5) + 1) if all((i % j for j in range(2, i)))]
    result = []
    for i in primes:
        if is_left_and_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)