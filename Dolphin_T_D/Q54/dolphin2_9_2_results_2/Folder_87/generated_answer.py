def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable(primes, n):
    for i in range(n, 0, -1):
        if is_prime(int(str(n)[-i:] + str(n)[:-i])):
            primes.append(int(str(n)[-i:] + str(n)[:-i]))
    primes = list(set(primes))
    primes.sort(reverse=True)
    return primes

def all_right_truncatable_prime(t):
    x = t[39]
    right = [1]
    primes = right_truncatable([], right[0])
    answer = []
    for p in primes:
        if p < x and len(str(p)) > 1:
            answer.append(p)
    answer.sort(reverse=True)
    return answer