def all_right_truncatable_prime(nums):
    x = nums[30]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    result = []
    for p in primes:
        right_truncatable = True
        p_str = str(p)
        for i in range(len(p_str) - 1, 0, -1):
            if not is_prime(int(p_str[:i])):
                right_truncatable = False
                break
        if right_truncatable:
            result.append(p)
    result.sort(reverse=True)
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True