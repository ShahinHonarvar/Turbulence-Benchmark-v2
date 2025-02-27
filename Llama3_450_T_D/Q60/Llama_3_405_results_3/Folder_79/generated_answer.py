def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[91]
    truncatable_primes = set()
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        num_str = str(num)
        for i in range(len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:-i] or num_str)
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                break
        else:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))