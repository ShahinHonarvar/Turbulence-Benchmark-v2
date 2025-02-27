def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[39]
    truncatable_primes = set()
    for num in range(10, x):
        if '0' not in str(num) and is_prime(num):
            truncatable = True
            n = num
            while n > 0:
                if not is_prime(n):
                    truncatable = False
                    break
                n //= 10
            if truncatable:
                truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)