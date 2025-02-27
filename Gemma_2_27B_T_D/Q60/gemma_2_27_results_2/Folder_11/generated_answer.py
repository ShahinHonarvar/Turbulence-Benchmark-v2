def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        if '0' not in str(i):
            is_truncatable = True
            n = i
            while n > 9:
                n = int(str(n)[1:])
                if not is_prime(n):
                    is_truncatable = False
                    break
            n = i
            while n > 9:
                n = int(str(n)[:-1])
                if not is_prime(n):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(i):
                primes.append(i)
    return sorted(primes)