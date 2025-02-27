def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[73]
    truncatable_primes = []
    for i in range(10, x):
        if '0' not in str(i) and is_prime(i):
            j = str(i)
            while len(j) > 1:
                j = j[1:]
                if not is_prime(int(j)):
                    break
            else:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)