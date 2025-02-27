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

def all_right_truncatable_prime(numbers):
    x = numbers[7]
    right_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        if is_prime(num):
            is_right_truncatable = True
            for i in range(len(str_num)):
                truncated_num = int(str_num[:-i - 1]) if i < len(str_num) - 1 else int(str_num)
                if not is_prime(truncated_num):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)