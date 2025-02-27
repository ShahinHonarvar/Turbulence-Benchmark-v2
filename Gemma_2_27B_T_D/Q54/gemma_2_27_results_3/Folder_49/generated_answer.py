from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[14]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            flag = True
            s = str(i)
            for j in range(1, len(s)):
                if not is_prime(int(s[:-j])):
                    flag = False
                    break
            if flag:
                primes.append(i)
    return sorted(primes)