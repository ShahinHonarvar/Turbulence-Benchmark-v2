def all_right_truncatable_prime(nums):
    x = nums[466]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            s = str(i)
            truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[:-j])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True