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

def all_right_truncatable_prime(tup):
    x = tup[25]
    right_truncatable_primes = set()
    for num in range(11, x):
        str_num = str(num)
        if is_prime(num):
            truncatable = True
            for i in range(1, len(str_num)):
                trunc_num = int(str_num[:-i])
                if not is_prime(trunc_num):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.add(num)
    return sorted(list(right_truncatable_primes), reverse=True)