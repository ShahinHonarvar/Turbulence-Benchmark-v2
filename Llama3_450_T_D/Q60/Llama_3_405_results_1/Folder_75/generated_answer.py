def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    truncatable_primes = set()
    for num in range(11, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable_prime = True
        for i in range(len(num_str)):
            trunc_left = int(num_str[i:])
            trunc_right = int(num_str[:-i or None])
            if not (is_prime(trunc_left) and is_prime(trunc_right)):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))