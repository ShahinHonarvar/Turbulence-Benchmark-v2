def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0 or n < 2:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(t):
    x = t[175]
    left_right_truncatable_primes = []
    for y in range(2, x + 1):
        if '0' in str(y):
            continue
        to_remove = len(str(y)) - (1 if len(str(y)) == 1 else 2)
        for i in range(to_remove):
            if not is_prime(int(str(y)[1:-1])):
                break
            y = int(str(y)[1:-1])
        else:
            left_right_truncatable_primes.append(y)
    return sorted(left_right_truncatable_primes)