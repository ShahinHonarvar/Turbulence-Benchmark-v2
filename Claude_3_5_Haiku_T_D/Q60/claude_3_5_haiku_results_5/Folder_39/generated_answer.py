def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[30]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        temp_left = num
        while temp_left > 0:
            if not is_prime(temp_left):
                is_left_right_truncatable = False
                break
            temp_left //= 10
        temp_right = num
        digit_count = len(str(num))
        while digit_count > 1:
            temp_right %= 10 ** (digit_count - 1)
            if not is_prime(temp_right):
                is_left_right_truncatable = False
                break
            digit_count -= 1
        if is_left_right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)