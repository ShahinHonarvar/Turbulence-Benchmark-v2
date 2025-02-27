from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(x):
    primes = []
    for num in count(1):
        if num >= x:
            break
        if is_prime(num):
            primes.append(num)
    result = []
    for prime in primes:
        num = prime
        while num:
            if not is_prime(num):
                break
            result.append(num)
            num = num // 10
    return sorted(result, reverse=True)

def all_left_truncatable_prime(tpl):
    return left_truncatable_primes(tpl[1])