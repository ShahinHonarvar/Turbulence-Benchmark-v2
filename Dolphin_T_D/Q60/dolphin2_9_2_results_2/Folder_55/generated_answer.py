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

def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    primes = []
    for i in range(x, 1, -1):
        if 0 in str(i):
            continue
        ii = i
        while len(str(ii)) > 1 and is_prime(ii):
            ii = int(str(ii)[1:])
        if len(str(ii)) == 1 and is_prime(ii):
            ii = i
            while len(str(ii)) > 1 and is_prime(ii):
                ii = int(str(ii)[:-1])
            if len(str(ii)) == 1 and is_prime(ii) and (i not in primes):
                primes.append(i)
    return sorted(primes, reverse=True)