from math import sqrt

def all_left_truncatable_prime(nums):
    x = nums[46]
    primes = []

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
    for num in range(2, x):
        if is_prime(num) and str(num).find('0') == -1:
            truncatable = True
            n = int(str(num)[:-1])
            while n > 1:
                if not is_prime(n):
                    truncatable = False
                    break
                n = int(str(n)[:-1])
            if truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)