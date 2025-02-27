def is_prime(num):
    if num > 3 and num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def truncate(num, i):
    return int(str(num)[i:])

def left_right_truncatable_prime(n):
    primes = []
    for num in range(1, n + 1):
        if is_prime(num):
            snum = str(num)
            if all((is_prime(int(snum[i:])) and is_prime(int(snum[:i + 1])) for i in range(len(snum) - 1))):
                primes.append(num)
    return sorted(primes, reverse=True)

def all_left_right_truncatable_prime(x):
    if isinstance(x, tuple) and len(x) > 37:
        x = x[37]
    else:
        x = int(x)
    return left_right_truncatable_prime(x)