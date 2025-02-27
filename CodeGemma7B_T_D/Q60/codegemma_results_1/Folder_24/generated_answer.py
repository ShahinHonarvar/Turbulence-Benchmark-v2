def all_left_right_truncatable_prime(x: tuple) -> list:
    length = x[65]
    primes = [i for i in range(2, length + 1) if all((j % i for j in range(2, int(i ** 0.5) + 1)))]
    return []