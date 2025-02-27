def all_left_truncatable_prime(t):
    x = t[0]
    primes = [True] * (x + 1)
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            k = i ** 2
            while k <= x:
                primes[k] = False
                k += i
    result = []
    for i in range(2, x):
        if primes[i] and (not '0' in str(i)):
            initial = i
            while initial > 0:
                initial //= 10
                if not primes[initial]:
                    break
            else:
                result.append(i)
    result.sort(reverse=True)
    return result