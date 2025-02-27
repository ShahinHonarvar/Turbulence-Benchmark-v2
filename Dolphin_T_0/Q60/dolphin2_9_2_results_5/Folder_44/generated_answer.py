def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[39]
    primes = []
    for n in range(2, x + 1):
        if is_prime(n) and '0' not in str(n):
            trunc = n
            while len(str(trunc)) > 2:
                trunc = int(str(trunc)[1:-1])
                if not is_prime(trunc):
                    break
            else:
                primes.append(n)
    return sorted(primes)