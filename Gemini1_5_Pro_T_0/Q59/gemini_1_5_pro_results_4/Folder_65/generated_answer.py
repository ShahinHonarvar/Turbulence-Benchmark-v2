def all_left_truncatable_prime(numbers):
    x = numbers[32]

    def is_left_truncatable_prime(n):
        if n < 10 and n in [2, 3, 5, 7]:
            return True
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            if int(s) not in primes:
                return False
            s = s[1:]
        if int(s) in primes:
            return True
        return False
    primes = []
    for i in range(2, x):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    result = []
    for p in primes:
        if is_left_truncatable_prime(p):
            result.append(p)
    return result