def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if n_str[i] == '0' or not is_prime(n_str[:i + 1]):
                return False
        return True

    def is_prime(n):
        n = int(n)
        if n > 1 and (not n % 2):
            n //= 2
            while n % 2 == 0:
                n //= 2
        if n >= 2:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
        return True
    x = numbers[975 - 1]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable = [i for i in primes if is_left_truncatable_prime(i)]
    left_truncatable.sort(reverse=True)
    return left_truncatable