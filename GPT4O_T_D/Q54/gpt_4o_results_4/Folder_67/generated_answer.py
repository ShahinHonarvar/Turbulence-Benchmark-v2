def all_right_truncatable_prime(numbers):
    if len(numbers) <= 71:
        return []
    x = numbers[71]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        str_n = str(n)
        while str_n:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)