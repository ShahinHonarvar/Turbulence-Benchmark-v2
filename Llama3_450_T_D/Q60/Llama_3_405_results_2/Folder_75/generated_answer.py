def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        is_truncatable_prime = True
        num_str = str(num)
        for i in range(1, len(num_str)):
            left_truncated = int(num_str[i:])
            right_truncated = int(num_str[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                is_truncatable_prime = False
                break
        if is_truncatable_prime and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)