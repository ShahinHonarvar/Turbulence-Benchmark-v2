def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        if '0' not in str(i):
            prime_str = str(i)
            truncatable = True
            while len(prime_str) > 1:
                if not is_prime(int(prime_str)):
                    truncatable = False
                    break
                prime_str = prime_str[1:]
            while len(prime_str) > 1:
                if not is_prime(int(prime_str)):
                    truncatable = False
                    break
                prime_str = prime_str[:-1]
            if truncatable and is_prime(i):
                primes.append(i)
    primes.sort()
    return primes