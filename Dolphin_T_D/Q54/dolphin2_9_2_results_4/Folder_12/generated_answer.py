def all_right_truncatable_prime(arr):
    x = arr[70]

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n in (1, 0):
            return False
        if n % 2 == 0:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        s = str(n)
        for i in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[i:])):
                return False
        return True
    primes = [n for n in range(2, x) if is_prime(n) and is_right_truncatable(n)]
    return sorted(primes, reverse=True)