def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[18]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        truncatable = True
        current = num
        while len(str(current)) > 1:
            current = int(str(current)[1:])
            if not is_prime(current):
                truncatable = False
                break
        current = num
        while len(str(current)) > 1:
            current = int(str(current)[:-1])
            if not is_prime(current):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)