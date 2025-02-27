def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[32]
    truncatable_primes = []
    for i in range(10, x + 1):
        if '0' in str(i):
            continue
        num_str = str(i)
        is_truncatable = True
        for j in range(len(num_str)):
            left_trunc = int(num_str[j:])
            right_trunc = int(num_str[:-j or None])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_truncatable = False
                break
        if is_truncatable and is_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)