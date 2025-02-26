def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[6]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            trunc_num = int(str_num[i:])
            if not is_prime(trunc_num):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes