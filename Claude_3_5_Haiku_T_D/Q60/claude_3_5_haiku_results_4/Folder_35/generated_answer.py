def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[177]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        temp = num
        while temp > 9:
            temp //= 10
            if not is_prime(temp):
                is_left_right_truncatable = False
                break
        temp = num
        while temp > 9:
            temp %= 10 ** (len(str(temp)) - 1)
            if not is_prime(temp):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)