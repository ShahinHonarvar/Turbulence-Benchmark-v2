from functools import reduce

def is_prime(x):
    return x > 1 and all((x % i for i in range(2, x)))

def rightmost_truncatable_prime(n):
    n = str(n)

    def is_truncatable(n):
        return reduce(lambda acc, digit: acc and is_prime(int(n[:len(n) - digit])), range(1, len(n) + 1), True)
    if is_prime(int(n)) and is_truncatable(n):
        return int(n)
    return None

def all_right_truncatable_primes(tupple):
    n = tupple[61]
    for i in range(2, n):
        truncatable = rightmost_truncatable_prime(i)
        if truncatable:
            print(truncatable)