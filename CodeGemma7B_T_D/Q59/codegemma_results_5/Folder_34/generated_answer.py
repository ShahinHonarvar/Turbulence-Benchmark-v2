def all_left_truncatable_prime(a):
    x = a[18]
    return sorted([i for i in range(2, x) if i not in [0, 2, 3, 5, 6, 8, 9] and all((isPrime(i - j) for j in range(10 ** (len(str(i)) - 1), i)))], reverse=True)

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True