def all_right_truncatable_prime(t: tuple) -> list:

    def is_prime(n: int) -> bool:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[429]
    primes = []
    for num in range(2, 10 ** 6):
        if is_prime(num):
            primes.append(num)
    right_truncatable_primes = []
    for num in primes:
        num_str = str(num)
        if len(num_str) > 1:
            for i in range(len(num_str) - 1):
                if is_prime(int(num_str[:-i])):
                    if int(num_str) < x:
                        right_truncatable_primes.append(int(num_str))
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes or []