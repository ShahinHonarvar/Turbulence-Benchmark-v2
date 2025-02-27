def all_right_truncatable_prime(numbers):
    x = numbers[618]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        s = str(n)
        for i in range(len(s)):
            if int(s[i:]) not in primes:
                return False
        return True
    primes = {2}
    for i in range(3, x):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(i)
    result = []
    for p in primes:
        if is_right_truncatable_prime(p):
            result.append(p)
    result.sort()
    return result