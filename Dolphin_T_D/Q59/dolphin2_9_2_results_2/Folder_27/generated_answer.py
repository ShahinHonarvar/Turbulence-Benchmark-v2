def all_left_truncatable_prime(tup):
    x = tup[79]
    primes = [2]
    for num in range(3, x):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)

    def is_truncatable(n):
        num = n
        while n:
            if n not in primes:
                return False
            n = n // 10
        if num not in primes:
            return False
        return True
    ret = [p for p in primes if is_truncatable(p)]
    return sorted(ret, reverse=True)