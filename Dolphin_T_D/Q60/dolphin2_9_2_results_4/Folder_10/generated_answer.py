def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[38]
    primes = []
    for n in range(x, 0, -1):
        digits = [int(d) for d in str(n)]
        if digits[0] == 0 or digits[-1] == 0:
            continue
        for _ in range(len(digits) - 1):
            if not is_prime(n):
                break
            n = n // 10
            n = n % 10
        if is_prime(n):
            primes.append(n)
    return primes