def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[92]
    primes = [2, 3, 5, 7]
    i = 10
    while i <= x:
        if is_prime(i):
            trunc = i
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(i)
        i += 1
    return sorted(primes)