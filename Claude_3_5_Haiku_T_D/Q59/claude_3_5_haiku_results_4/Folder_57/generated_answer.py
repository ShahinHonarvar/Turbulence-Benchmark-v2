def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[54]
    left_truncatable_primes = []
    for num in range(x):
        if '0' not in str(num):
            truncatable = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    truncatable = False
                    break
                temp //= 10
            if truncatable and is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)