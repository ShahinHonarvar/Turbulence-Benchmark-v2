def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(n):
        return all((is_prime(n) for n in (int(str(n)[i:]) for i in range(len(str(n))))))
    x = numbers[28]
    primes = [n for n in range(2, x) if is_prime(n) and is_truncanable(n)]
    return sorted(primes)