def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_truncatable(prime):
    if '0' in str(prime):
        return False
    str_prime = str(prime)
    for i in range(1, len(str_prime)):
        if not (is_prime(int(str_prime[i:])) and is_prime(int(str_prime[:-i]))):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[784]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return truncatable_primes