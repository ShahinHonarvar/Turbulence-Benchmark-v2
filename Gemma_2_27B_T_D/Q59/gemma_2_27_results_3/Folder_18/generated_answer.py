def all_left_truncatable_prime(t):
    x = t[429]
    primes = []
    for num in range(x, 1, -1):
        if str(num).count('0') == 0 and all((int(str(num)[i:]) in [2, 3, 5, 7] or is_prime(int(str(num)[i:])) for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True