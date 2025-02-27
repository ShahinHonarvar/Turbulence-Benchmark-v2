def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[29]
    primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i):
            trunc = i
            while len(str(trunc)) > 1:
                trunc = int(str(trunc)[1:-1])
                if not is_prime(trunc):
                    break
                if len(str(trunc)) == 1:
                    primes.append(i)
                    break
    return sorted(primes)