def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[65]
    left_primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            for j in str(i):
                if j == '0':
                    break
                if not is_prime(int(str(i).replace(j, ''))):
                    break
            else:
                left_primes.append(i)
    return sorted(left_primes, reverse=True)