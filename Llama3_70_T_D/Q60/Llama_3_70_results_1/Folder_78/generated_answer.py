def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[23]
    primes = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        str_n = str(n)
        is_truncatable = True
        for i in range(1, len(str_n)):
            left_trunc = int(str_n[i:])
            right_trunc = int(str_n[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_truncatable = False
                break
        if is_truncatable and is_prime(n):
            primes.append(n)
    return primes