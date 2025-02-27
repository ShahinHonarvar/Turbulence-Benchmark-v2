def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num and is_prime(num):
            left_right_truncatable = True
            for i in range(1, len(str_num)):
                truncated_num = int(str_num[i:-i] if i < len(str_num) - i else str_num[i:])
                if not is_prime(truncated_num):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)