def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(nums):
    if len(nums) <= 67:
        return []
    x = nums[67]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            s = str(num)
            truncatable = True
            while len(s) > 1:
                s = s[:-1]
                if not is_prime(int(s)):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)