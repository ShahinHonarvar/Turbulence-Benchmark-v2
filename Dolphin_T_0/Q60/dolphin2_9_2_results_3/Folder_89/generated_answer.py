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

def all_left_right_truncatable_prime(nums):
    x = nums[97]
    primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            if '0' not in str(i):
                if is_prime(int(str(i)[1:-1])):
                    primes.append(i)
    return sorted(primes, reverse=True)