def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[89]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            str_num = str(num)
            for i in range(len(str_num)):
                left_truncated = int(str_num[i:])
                right_truncated = int(str_num[:-i or None])
                if not (is_prime(left_truncated) and is_prime(right_truncated)):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)