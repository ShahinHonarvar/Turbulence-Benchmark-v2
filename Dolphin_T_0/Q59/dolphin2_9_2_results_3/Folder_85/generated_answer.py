def all_left_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [2]
    res = []
    i = 3
    while True:
        if all((int(str(i)[j:]) for j in range(1, len(str(i))))):
            primes.append(i)
        i += 2
        if i > n:
            break
    primes.reverse()
    for prime in primes:
        if int(str(prime)[0:1]) not in primes:
            primes.remove(int(str(prime)[0:1]))
    res.extend([i for i in primes if i < n])
    return sorted(res)