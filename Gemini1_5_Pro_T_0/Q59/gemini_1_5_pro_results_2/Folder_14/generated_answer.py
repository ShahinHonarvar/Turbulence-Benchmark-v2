def all_left_truncatable_prime(numbers):
    x = numbers[78]

    def is_left_truncatable_prime(num):
        if num < 10 and num > 0:
            return num in [2, 3, 5, 7]
        if '0' in str(num):
            return False
        s = str(num)
        for i in range(1, len(s)):
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