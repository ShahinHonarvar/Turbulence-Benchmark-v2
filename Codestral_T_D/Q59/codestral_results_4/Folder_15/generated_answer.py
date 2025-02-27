def all_left_truncatable_prime(numbers):
    x = numbers[6]
    left_truncatable_primes = []
    for num in range(2, x):
        if str(num).count('0') == 0:
            truncated_num = num
            is_left_truncatable = True
            while truncated_num > 0:
                truncated_num //= 10
                if truncated_num > 0 and (not is_prime(truncated_num)):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True