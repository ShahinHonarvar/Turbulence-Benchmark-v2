def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[429]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            num = i
            while num != 0 and is_prime(num):
                num //= 10
                if num != 0:
                    primes.append(i)
    return sorted(primes, reverse=True)