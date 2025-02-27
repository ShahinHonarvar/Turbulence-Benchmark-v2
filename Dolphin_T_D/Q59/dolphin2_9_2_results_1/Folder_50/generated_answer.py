def all_left_truncatable_prime(data):
    x = data[57]
    primes = [2, 3, 5, 7]
    for v in range(9, x, 2):
        v = str(v)
        if '0' in v:
            continue
        for i in range(len(v)):
            if not is_prime(int(v[i:])):
                break
        else:
            primes.append(int(v))
    first = 3
    primes.sort(reverse=True)
    while all_left_truncatable_prime(primes[first:]):
        primes = primes[:first]
        first += 1
    return primes

def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True