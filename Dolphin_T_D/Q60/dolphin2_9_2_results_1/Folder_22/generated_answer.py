def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = numbers[85]
    primes = []
    for n in range(2, x + 1):
        if is_prime(n) and str(n).isdigit() and all((is_prime(int(str(n)[i:j])) for i in range(len(str(n))) for j in range(i + 1, len(str(n)) + 1))):
            primes.append(n)
    return sorted(primes)