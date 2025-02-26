def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[618]
    truncatable_primes = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        is_left_right_truncatable = True
        temp = n
        while temp > 0:
            if not is_prime(temp):
                is_left_right_truncatable = False
                break
            temp //= 10
        temp = n
        digit_length = len(str(n))
        while digit_length > 1:
            temp %= 10 ** (digit_length - 1)
            if not is_prime(temp):
                is_left_right_truncatable = False
                break
            digit_length -= 1
        if is_left_right_truncatable and is_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)