def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(n):
    primes = []
    for i in range(1, n):
        if is_prime(i):
            for j in range(len(str(i)), 0, -1):
                if not is_prime(int(str(i)[j - 1:])):
                    break
            else:
                primes.append(i)
    return primes

def all_left_truncatable_prime(t):
    x = 10 ** 18
    for i in t:
        if i > 10 ** 18:
            break
        x = i
    return sorted(left_truncatable_primes(x))