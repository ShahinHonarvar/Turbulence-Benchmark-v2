def all_right_truncatable_prime(tup):
    x = tup[945]
    right_truncatable_primes = []
    for i in range(10 ** (len(str(x)) - 1), 10 ** len(str(x))):
        if is_prime(i) and is_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True