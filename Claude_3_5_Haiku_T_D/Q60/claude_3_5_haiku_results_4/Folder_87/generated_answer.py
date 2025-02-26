def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[39]
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
        div = 10
        while current > 0:
            current %= div
            if not is_prime(current):
                is_left_right_truncatable = False
                break
            div *= 10
        if is_left_right_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes