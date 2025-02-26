def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[175]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        is_truncatable = True
        left = num
        while left > 0:
            if not is_prime(left):
                is_truncatable = False
                break
            left //= 10
        right = num
        while right > 0:
            if not is_prime(right):
                is_truncatable = False
                break
            right %= 10 ** (len(str(right)) - 1)
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)