def all_left_truncatable_prime(numbers):
    x = numbers[65]

    def is_left_truncatable_prime(n):
        if n < 10:
            return n in [2, 3, 5, 7]
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if int(s[i:]) not in prime_numbers:
                return False
        return True
    prime_numbers = [2]
    for i in range(3, x):
        is_prime = True
        for j in prime_numbers:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    left_truncatable_primes = []
    for p in prime_numbers:
        if is_left_truncatable_prime(p):
            left_truncatable_primes.append(p)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes