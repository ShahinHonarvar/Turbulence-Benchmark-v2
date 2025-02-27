def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[20]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        for i in range(1, len(str_num)):
            truncated_num1 = int(str_num[i:])
            truncated_num2 = int(str_num[:-i])
            if not is_prime(truncated_num1) or not is_prime(truncated_num2):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)