def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[18]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            is_truncatable = True
            truncated = num
            while len(str(truncated)) > 1:
                truncated = int(str(truncated)[1:])
                if not is_prime(truncated):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)