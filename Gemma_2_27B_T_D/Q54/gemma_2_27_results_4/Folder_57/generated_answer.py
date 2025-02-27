def all_right_truncatable_prime(nums):
    x = nums[54]
    primes = []
    for i in range(2, x):
        flag = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            primes.append(i)
    result = []
    for p in primes:
        p_str = str(p)
        is_truncatable = True
        for i in range(len(p_str) - 1, 0, -1):
            if not is_prime(int(p_str[:i])):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(p)
    return sorted(result, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True