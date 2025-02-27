def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[54]
    primes = []
    for i in range(2, x):
        if is_prime(i) and str(i).count('0') == 0:
            j = i
            while j > 0:
                if not is_prime(int(str(j)[1:])):
                    break
                j = int(str(j)[1:])
            else:
                primes.append(i)
    return sorted(primes, reverse=True)