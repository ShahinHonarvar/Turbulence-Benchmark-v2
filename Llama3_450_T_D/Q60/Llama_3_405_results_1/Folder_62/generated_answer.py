def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        left_right_truncatable = True
        num_str = str(num)
        for i in range(1, len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                left_right_truncatable = False
                break
        if left_right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)