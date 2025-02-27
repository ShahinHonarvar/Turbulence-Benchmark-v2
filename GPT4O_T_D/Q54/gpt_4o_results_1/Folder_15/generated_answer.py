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

def right_truncatable_primes_below(n):

    def is_right_truncatable_prime(num):
        str_num = str(num)
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[:-1]
        return True
    result = []
    for i in range(2, n):
        if is_right_truncatable_prime(i):
            result.append(i)
    return result

def all_right_truncatable_prime(t):
    if len(t) <= 6:
        return []
    x = t[6]
    primes = right_truncatable_primes_below(x)
    return sorted(primes, reverse=True)