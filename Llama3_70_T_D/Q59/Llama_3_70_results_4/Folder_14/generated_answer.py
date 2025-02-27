def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[78]
    truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        trunc_num = str(num)
        is_truncatable_prime = True
        while len(trunc_num) > 1:
            trunc_num = trunc_num[1:]
            if not is_prime(int(trunc_num)):
                is_truncatable_prime = False
                break
        if is_truncatable_prime and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)