def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[22]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        temp_left = num
        temp_right = num
        while temp_left > 9:
            temp_left //= 10
            if not is_prime(temp_left):
                is_truncatable = False
                break
        while temp_right > 9:
            temp_right %= 10 ** (len(str(temp_right)) - 1)
            if not is_prime(temp_right):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num) and is_prime(temp_left):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)