import bisect

def all_right_truncatable_prime(n):
    if n[54] < 2:
        return []
    primes = [2]
    for i in range(2, int(n[54]) + 1):
        if all((p % i != 0 for p in primes)):
            primes.append(i)
    for p in primes:
        if p * p <= n[54]:
            break
    else:
        primes.append(n[54])
    primes.sort()
    for p in primes:
        if p * p <= n[54]:
            break
    else:
        primes.append(n[54])
    return primes[:bisect.bisect_right(primes, n[54])]