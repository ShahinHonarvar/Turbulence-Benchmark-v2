def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[24]
    truncatable_primes = set()
    for num in range(10, x):
        str_num = str(num)
        if is_prime(num):
            truncatable = True
            for i in range(len(str_num) - 1, 0, -1):
                trunc_num = int(str_num[:i])
                if not is_prime(trunc_num):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.add(num)
    return sorted(list(truncatable_primes))