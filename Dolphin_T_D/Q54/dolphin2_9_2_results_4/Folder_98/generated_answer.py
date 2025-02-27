def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(t):
    x = t[8]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable = []
    for p in primes:
        q = p
        while q != 0:
            if is_prime(q):
                q = q // 10
            else:
                break
        else:
            right_truncatable.append(p)
    return sorted(right_truncatable, reverse=True)