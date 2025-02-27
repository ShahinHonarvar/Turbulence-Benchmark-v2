def is_prime(n):
    if n < 2:
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
    x = numbers[46]
    left_right_truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            is_prime_num = True
            for i in range(len(str_num) - 1):
                left_truncated_num = int(str_num[i + 1:])
                right_truncated_num = int(str_num[:len(str_num) - i - 1])
                if not is_prime(left_truncated_num) or not is_prime(right_truncated_num):
                    is_prime_num = False
                    break
            if is_prime_num:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)