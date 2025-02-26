def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[429]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            str_num = str(num)
            is_truncatable = True
            for i in range(len(str_num) - 1, 0, -1):
                truncated = int(str_num[:i])
                if not is_prime(truncated):
                    is_truncatable = False
                    break
            if is_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)