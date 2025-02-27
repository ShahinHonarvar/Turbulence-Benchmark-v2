def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = numbers[50]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            s = str(i)
            if all((is_prime(int(s[j:])) for j in range(len(s) - 1))):
                primes.append(i)
    return sorted(primes, reverse=True)