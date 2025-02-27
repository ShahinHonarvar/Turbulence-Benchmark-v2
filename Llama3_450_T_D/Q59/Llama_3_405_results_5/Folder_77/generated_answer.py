def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[767]
    left_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        if '0' not in str_num:
            truncatable = True
            for i in range(len(str_num)):
                trunc_num = int(str_num[i:])
                if not is_prime(trunc_num):
                    truncatable = False
                    break
            if truncatable and is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)