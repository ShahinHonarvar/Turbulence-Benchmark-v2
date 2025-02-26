def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[50]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        current = num
        while current > 0:
            if not is_prime(current):
                is_left_right_truncatable = False
                break
            current //= 10
        current = num
        digits = len(str(current))
        while digits > 1:
            current %= 10 ** (digits - 1)
            if not is_prime(current):
                is_left_right_truncatable = False
                break
            digits -= 1
        if is_left_right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)