def all_left_truncatable_prime(numbers):
    x = numbers[57]

    def is_left_truncatable_prime(n):
        if n < 10 and n in (2, 3, 5, 7):
            return True
        if '0' in str(n) or n < 10:
            return False
        s = str(n)
        while len(s) > 0:
            if int(s) not in primes:
                return False
            s = s[1:]
        return True
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    left_truncatable_primes = []
    for prime in primes:
        if is_left_truncatable_prime(prime):
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes