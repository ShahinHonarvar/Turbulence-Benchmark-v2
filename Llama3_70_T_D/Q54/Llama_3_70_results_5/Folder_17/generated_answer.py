def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[36]
    rt_primes = []
    for num in range(10, x):
        is_rt_prime = True
        temp = str(num)
        while temp:
            if not is_prime(int(temp)):
                is_rt_prime = False
                break
            temp = temp[:-1]
        if is_rt_prime:
            rt_primes.append(num)
    return sorted(rt_primes, reverse=True)