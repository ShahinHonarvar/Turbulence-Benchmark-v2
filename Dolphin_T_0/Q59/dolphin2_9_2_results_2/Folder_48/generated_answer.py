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

def is_left_truncatable(n):
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[835]
    lt_primes = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]
    return sorted(lt_primes)