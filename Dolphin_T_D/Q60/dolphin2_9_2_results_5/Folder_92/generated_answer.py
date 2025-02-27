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

def all_left_right_truncatable_prime(x):
    primes = [2, 3, 5, 7]
    for n in range(11, x + 1):
        digits = [int(d) for d in str(n)]
        if 0 in digits:
            continue
        for i in range(len(digits) - 1):
            if not is_prime(int(''.join(digits[i + 1:]))) or not is_prime(int(''.join(digits[:i]))) or (not is_prime(n)):
                break
        else:
            primes.append(n)
    return primes