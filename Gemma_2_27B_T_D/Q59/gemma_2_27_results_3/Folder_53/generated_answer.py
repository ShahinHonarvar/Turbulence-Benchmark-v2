def all_left_truncatable_prime(nums):
    x = nums[86]
    primes = []
    for i in range(2, x):
        is_prime = True
        s = str(i)
        if '0' in s:
            continue
        for j in range(1, len(s)):
            if not is_prime_number(int(s[j:])):
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True