def all_left_truncatable_prime(numbers):
    x = numbers[39]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        elif not is_prime(n):
            return False
        elif '0' in str(n):
            return False
        else:
            return is_left_truncatable_prime(int(str(n)[1:]))
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)