def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    s = str(n)
    for i in range(len(s) - 1, 0, -1):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[1]
    primes = [i for i in range(x) if is_left_truncatable(i) and is_prime(i)]
    return sorted(primes)