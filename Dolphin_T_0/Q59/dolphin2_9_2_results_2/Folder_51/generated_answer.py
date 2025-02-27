def all_left_truncatable_prime(x):
    left_trunc_primes = []
    for num in range(2, x):
        if num == 0 or num == 1 or has_zero_in_it(num):
            continue
        else:
            trunc = num
            while trunc != 0:
                if not is_prime(trunc):
                    break
                trunc = trunc // 10
                if trunc != 0:
                    left_trunc_primes.append(num)
    left_trunc_primes.sort()
    return left_trunc_primes

def has_zero_in_it(n):
    while n != 0:
        if n % 10 == 0:
            return True
        else:
            n = n // 10
    return False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True