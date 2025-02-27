def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[618]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
                if trunc == 0:
                    primes.append(num)
                    break
    return sorted(primes)