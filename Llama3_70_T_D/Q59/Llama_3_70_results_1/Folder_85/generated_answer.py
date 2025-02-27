def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[94]
    lt_primes = []
    for num in range(11, x):
        if '0' in str(num):
            continue
        truncatable = True
        temp = str(num)
        while len(temp) > 1:
            temp = temp[1:]
            if not is_prime(int(temp)):
                truncatable = False
                break
        if truncatable and is_prime(num):
            lt_primes.append(num)
    return sorted(lt_primes)