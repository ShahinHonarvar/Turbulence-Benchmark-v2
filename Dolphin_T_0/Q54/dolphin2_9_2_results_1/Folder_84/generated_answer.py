def all_right_truncatable_prime(nums):
    x = nums[630]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            if is_right_truncatable(i):
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(p):
    p_str = str(p)
    for i in range(1, len(p_str)):
        if not is_prime(int(p_str[i:])):
            return False
    return True