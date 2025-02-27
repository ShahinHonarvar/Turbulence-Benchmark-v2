def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[39]
    primes = [2, 3, 7]
    for num in range(10, x):
        if is_prime(num):
            trunc = num
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(num)
    return sorted(primes)