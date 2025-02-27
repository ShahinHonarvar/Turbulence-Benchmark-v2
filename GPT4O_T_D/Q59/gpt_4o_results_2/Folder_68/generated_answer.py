def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_left_truncatable(prime):
    s = str(prime)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[1]
    lt_primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable(num):
            lt_primes.append(num)
    return sorted(lt_primes, reverse=True)