def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i ** 2 <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = numbers[52]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i) and is_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)