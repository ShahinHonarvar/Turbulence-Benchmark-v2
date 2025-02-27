def all_left_truncatable_prime(numbers):
    x = numbers[767]

    def is_left_truncatable_prime(n):
        if n < 10:
            return n in [2, 3, 5, 7]
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if int(s[i:]) not in primes:
                return False
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