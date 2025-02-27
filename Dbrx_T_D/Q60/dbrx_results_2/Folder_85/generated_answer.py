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

def all_left_right_truncatable_prime(limit_tuple):
    x = limit_tuple[94]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            primes.append(i)
    result = []
    for prime in primes:
        flag = True
        for j in range(len(str(prime)) - 1, 0, -1):
            if not is_prime(int(str(prime)[j:])):
                flag = False
                break
        if flag and str(prime)[0] != '0':
            result.append(prime)
    return sorted(result)