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
            truncated_nums = left_truncate(num)
            if all((is_prime(n) for n in truncated_nums)):
                primes.append(num)
    return sorted(primes)