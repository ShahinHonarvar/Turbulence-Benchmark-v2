def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[46]
    truncatable_primes = set()
    for num in range(11, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        truncatable = True
        for i in range(1, len(str_num)):
            trunc = int(str_num[i:])
            if not is_prime(trunc):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.add(num)
    return sorted(truncatable_primes, reverse=True)