def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[975]
    primes = []
    for num in range(x - 1, 0, -1):
        if is_prime(num):
            n = num
            while n:
                if is_prime(n):
                    n //= 10
                else:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)