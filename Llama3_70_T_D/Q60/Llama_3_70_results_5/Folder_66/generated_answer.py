def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[25]
    left_right_truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        is_left_right_truncatable_prime = True
        for i in range(1, len(num_str)):
            left_trunc_str = num_str[i:]
            right_trunc_str = num_str[:-i]
            if not (is_prime(int(left_trunc_str)) and is_prime(int(right_trunc_str))):
                is_left_right_truncatable_prime = False
                break
        if is_left_right_truncatable_prime and is_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)