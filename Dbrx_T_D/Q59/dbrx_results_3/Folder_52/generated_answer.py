from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes():
    for n in count():
        if is_prime(n):
            yield n

def all_left_truncatable_prime(t):
    x = t[52]
    primes = list(t[:52])
    result = []
    for i in left_truncatable_primes():
        if i >= x:
            break
        for j in range(len(str(i)), 0, -1):
            if int(str(i)[:j]) == 0 or not is_prime(int(str(i)[:j])):
                break
        else:
            result.append(i)
    return sorted(result, reverse=True)