def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    left_trunc = num
    right_trunc = num
    while left_trunc > 9:
        left_trunc //= 10
        if not is_prime(left_trunc):
            break
    while right_trunc > 9:
        right_trunc %= 10 ** len(str(right_trunc)) // 10
        if not is_prime(right_trunc):
            break
    return (left_trunc, right_trunc)

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num > 1 and num <= 73939133:
            left_trunc, right_trunc = left_right_truncate(num)
            if left_trunc == 2 and right_trunc == num:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)