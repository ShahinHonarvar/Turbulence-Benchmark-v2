def all_left_truncatable_prime(numbers):
    x = numbers[945]

    def is_left_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        s = str(n)
        while len(s) > 0:
            if int(s) not in prime_numbers:
                return False
            s = s[1:]
        return True
    prime_numbers = [2]
    for i in range(3, x):
        is_prime = True
        for p in prime_numbers:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    left_truncatable_primes = []
    for p in prime_numbers:
        if is_left_truncatable_prime(p):
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)