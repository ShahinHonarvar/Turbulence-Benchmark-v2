def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[25]
    truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            temp = str(num)
            for i in range(len(temp)):
                if not is_prime(int(temp[i:])):
                    truncatable = False
                    break
            if truncatable and is_prime(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)