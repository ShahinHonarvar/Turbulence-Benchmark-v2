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

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[29]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            if not '0' in s and len(s) > 1:
                left_right_truncatable = True
                for j in range(len(s) - 1):
                    if not is_prime(int(s[1 + j:])) or not is_prime(int(s[:-1 - j])):
                        left_right_truncatable = False
                        break
                if left_right_truncatable:
                    primes.append(i)
    return sorted(primes)