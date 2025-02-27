def all_right_truncatable_prime(nums):
    x = nums[792]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            k = str(num)
            for i in range(1, len(k)):
                if not is_prime(int(k[:-i])):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort()
    return right_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True