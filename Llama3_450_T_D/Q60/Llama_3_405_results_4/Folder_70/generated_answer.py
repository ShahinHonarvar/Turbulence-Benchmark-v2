def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        left_right_truncatable = True
        num_str = str(num)
        for i in range(len(num_str)):
            trunc_left = int(num_str[i:])
            trunc_right = int(num_str[:-i or None])
            if not (is_prime(trunc_left) and is_prime(trunc_right)):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)