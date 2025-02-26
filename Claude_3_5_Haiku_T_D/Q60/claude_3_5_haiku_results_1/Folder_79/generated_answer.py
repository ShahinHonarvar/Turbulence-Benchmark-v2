def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[91]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        is_truncatable = True
        for length in range(len(str(num)) - 1, 0, -1):
            trunc = int(str(num)[1:])
            if not is_prime(trunc):
                is_truncatable = False
                break
            num = trunc
        num = nums[91]
        for length in range(len(str(num)) - 1, 0, -1):
            trunc = int(str(num)[:-1])
            if not is_prime(trunc):
                is_truncatable = False
                break
            num = trunc
        if is_truncatable:
            truncatable_primes.append(nums[91])
    return sorted(truncatable_primes)