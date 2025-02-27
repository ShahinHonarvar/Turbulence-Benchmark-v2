def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(t):
    x = t[93]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(num)
    return sorted(primes)