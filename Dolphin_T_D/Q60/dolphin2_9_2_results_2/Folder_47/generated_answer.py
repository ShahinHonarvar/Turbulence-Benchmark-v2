def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(1, x + 1):
        digits = list(map(int, str(num)))
        if 0 in digits:
            continue
        while len(digits) > 2:
            if not is_prime(int(''.join(map(str, digits)))):
                break
            digits.pop(0)
            digits.pop()
        if is_prime(num):
            primes.append(num)
    return primes