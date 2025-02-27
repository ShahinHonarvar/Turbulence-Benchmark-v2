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

def all_left_truncatable_prime(t):
    x = t[70]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and (not '0' in str(i)):
            j = i
            while j > 1:
                if not is_prime(j):
                    break
                j = int(str(j)[1:])
                if j < 2:
                    break
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)