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
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            str_num = str(num)
            truncatable = True
            i = 1
            while i < len(str_num):
                if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                    truncatable = False
                    break
                i += 1
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)