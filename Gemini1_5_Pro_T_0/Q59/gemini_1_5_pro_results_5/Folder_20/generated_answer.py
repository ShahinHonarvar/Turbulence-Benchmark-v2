def all_left_truncatable_prime(numbers):
    x = numbers[100]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 0:
            return n > 1
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s) + 1):
            if int(s[i - 1:]) not in primes:
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
    result = []
    for prime in primes:
        if is_left_truncatable_prime(prime):
            result.append(prime)
    result.sort(reverse=True)
    return result