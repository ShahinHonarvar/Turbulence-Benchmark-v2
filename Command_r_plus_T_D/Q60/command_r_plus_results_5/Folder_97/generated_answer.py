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

def is_left_right_truncatable_prime(n):
    if str(n).count('0') > 0:
        return False
    str_n = str(n)
    while len(str_n) > 1:
        if not is_prime(int(str_n)) or not is_prime(int(str_n[::-1])):
            return False
        str_n = str_n[1:]
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[645]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)