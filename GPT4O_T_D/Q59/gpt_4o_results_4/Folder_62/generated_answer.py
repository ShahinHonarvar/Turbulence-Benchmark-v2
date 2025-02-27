def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    if not is_prime(num):
        return False
    temp = str(num)
    while len(temp) > 1:
        temp = temp[1:]
        if not is_prime(int(temp)):
            return False
    return True

def all_left_truncatable_prime(nums):
    if len(nums) <= 70:
        return []
    x = nums[70]
    primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return primes