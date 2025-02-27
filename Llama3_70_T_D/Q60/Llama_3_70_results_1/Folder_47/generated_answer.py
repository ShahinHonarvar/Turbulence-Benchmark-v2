def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[49]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        str_i = str(i)
        if '0' in str_i:
            continue
        if not is_prime(i):
            continue
        truncated = True
        for j in range(1, len(str_i)):
            if not is_prime(int(str_i[j:])) or not is_prime(int(str_i[:-j])):
                truncated = False
                break
        if truncated:
            left_right_truncatable_primes.append(i)
    return left_right_truncatable_primes