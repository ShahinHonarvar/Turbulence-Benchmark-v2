def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncated_primes(n):
    s = str(n)
    return all((is_prime(int(s[i:])) and is_prime(int(s[:i + 1])) for i in range(len(s))))

def all_left_right_truncatable_prime(t):
    x = t[992]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and truncated_primes(num):
            result.append(num)
    return result