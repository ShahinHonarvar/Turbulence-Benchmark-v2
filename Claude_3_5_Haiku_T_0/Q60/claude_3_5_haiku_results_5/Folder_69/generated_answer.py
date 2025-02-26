def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[760]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        for i in range(len(str(num)), 0, -1):
            if not is_prime(int(str(num)[:i])):
                is_truncatable = False
                break
        if is_truncatable:
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    is_truncatable = False
                    break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)