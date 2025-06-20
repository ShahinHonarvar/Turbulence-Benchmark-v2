def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[0]
    truncatable_primes = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            is_truncatable = True
            for i in range(1, len(str_num)):
                left_truncation = int(str_num[i:])
                right_truncation = int(str_num[:-i])
                if not is_prime(left_truncation) or not is_prime(right_truncation):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)