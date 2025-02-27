def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(p):
    x = p[1]
    left_trunc_primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            trunc_str = str(num)
            while len(trunc_str) > 1 and is_prime(int(trunc_str)):
                trunc_str = trunc_str[1:]
                if is_prime(int(trunc_str)):
                    left_trunc_primes.append(num)
    left_trunc_primes = list(set(left_trunc_primes))
    left_trunc_primes.sort(reverse=True)
    return left_trunc_primes