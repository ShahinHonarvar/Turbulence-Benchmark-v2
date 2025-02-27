def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[32]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if is_prime(num):
            num = str(num)
            if '0' in num or not all((is_prime(int(num[i:j])) for i in range(len(num)) for j in range(i + 1, len(num) + 1))):
                continue
            primes.append(int(num))
    return sorted(primes)