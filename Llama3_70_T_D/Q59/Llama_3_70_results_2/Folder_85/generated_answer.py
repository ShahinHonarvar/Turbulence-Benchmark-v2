def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[94]
    left_truncatable_primes = []
    for num in range(11, x):
        if '0' not in str(num):
            is_truncatable = True
            str_num = str(num)
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)