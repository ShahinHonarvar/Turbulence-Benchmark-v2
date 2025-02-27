def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if str(n)[0] == '0' or str(n)[-1] == '0':
            return False
        n = str(n)
        while len(n) > 1:
            if not is_prime(int(n)):
                return False
            n = n[1:-1]
        return True
    x = numbers[55]
    primes = [n for n in range(2, x + 1) if is_prime(n) and is_truncatable(n)]
    return sorted(primes, reverse=True)