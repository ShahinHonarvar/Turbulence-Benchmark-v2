def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncate(num):
    str_num = str(num)
    return [int(str_num[:i]) for i in range(1, len(str_num))]

def all_left_truncatable_prime(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            left_truncatable = all((is_prime(n) for n in left_truncate(num)))
            no_zero = str(num).count('0') == 0
            if left_truncatable and no_zero:
                primes.append(num)
    return sorted(primes)