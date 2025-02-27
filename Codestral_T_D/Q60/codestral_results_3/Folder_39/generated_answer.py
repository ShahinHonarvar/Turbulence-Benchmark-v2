def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp //= 10
        temp = n
        while temp >= 10:
            temp %= 10 ** (len(str(temp)) - 1)
            if not is_prime(temp):
                return False
        return True
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes