def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = numbers[43]
    primes = [n for n in range(2, x + 1) if is_prime(n)]

    def is_truncatable(n):
        n = str(n)
        return all((is_prime(int(n[i:j])) for i in range(len(n)) for j in range(i + 1, len(n) + 1)))
    return sorted([n for n in primes if int(n) < x and is_truncatable(n)])