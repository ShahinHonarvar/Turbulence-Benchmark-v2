def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[3]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            j = i
            while j > 9:
                if not is_prime(j // 10) or not is_prime(j % 10):
                    break
                j //= 10
                j %= 10 ** (len(str(i)) - 1)
            else:
                primes.append(i)
    return primes