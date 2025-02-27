def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        sqrt_n = int(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True

def all_right_truncatable_prime(x):
    primes = []
    for num in range(x, 1, -1):
        if len(primes) == 0:
            primes.append(num)
        else:
            str_num = str(num)
            if len(str_num) > 1 and int(str_num[1:]) in primes and all([is_prime(int(str_num[:-i])) for i in range(1, len(str_num))]):
                primes.append(num)
    return sorted(primes, reverse=True)