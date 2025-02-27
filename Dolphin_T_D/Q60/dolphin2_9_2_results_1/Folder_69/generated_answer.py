def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[760]
    primes = []
    for num in range(x, 1, -1):
        if not '0' in str(num) and is_prime(num):
            removable = set(str(num))
            removable.remove(str(num)[0])
            removable.remove(str(num)[-1])
            removable = list(map(int, removable))
            if all((is_prime(int(''.join((str(val) for val in num[:i] + num[i + 1:])))) for i in removable)):
                primes.append(num)
    return sorted(primes, reverse=True)