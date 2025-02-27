def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    n = x[86]
    primes = []
    for i in range(2, n + 1):
        num = i
        while num != 0:
            if num != i and is_prime(num) and (num != 1 or i != num):
                primes.append(i)
                break
            num = int(num / 10)
    return sorted(list(set(primes)))