from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable_primes(nums):
    primes = []
    for num in nums:
        if is_prime(num):
            temp = num
            while temp > 0:
                if not is_prime(temp % 10):
                    break
                temp //= 10
            else:
                primes.append(num)
    return sorted(primes, reverse=True)