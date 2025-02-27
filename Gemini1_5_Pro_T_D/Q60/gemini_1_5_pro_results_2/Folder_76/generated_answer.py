def all_left_right_truncatable_prime(numbers):
    x = numbers[370]

    def is_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if int(s[i:]) not in primes or int(s[:-i]) not in primes:
                return False
        return True
    primes = {2}
    for num in range(3, x + 1, 2):
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(num)
    truncatable_primes = []
    for p in primes:
        if is_truncatable_prime(p):
            truncatable_primes.append(p)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes