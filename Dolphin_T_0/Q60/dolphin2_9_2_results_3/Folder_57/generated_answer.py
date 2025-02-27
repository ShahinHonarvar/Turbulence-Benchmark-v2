def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        trunc = len(str(num))
        trunc = 1 if trunc == 1 else 2 if trunc == 2 else 0
        while trunc > 0:
            if not is_prime(trunc):
                break
            trunc = int(str(trunc)[1:-1])
        else:
            primes.append(num)
    return list(reversed(sorted(primes)))