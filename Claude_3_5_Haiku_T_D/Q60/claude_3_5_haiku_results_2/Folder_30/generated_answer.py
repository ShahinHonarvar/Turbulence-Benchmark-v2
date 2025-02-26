def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        left = int(str(n)[i:])
        right = int(str(n)[:len(str(n)) - i])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[37]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes