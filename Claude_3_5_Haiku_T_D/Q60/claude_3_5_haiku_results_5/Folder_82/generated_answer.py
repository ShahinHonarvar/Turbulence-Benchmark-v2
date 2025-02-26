def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 9:
        n_str = str(n)
        n = int(n_str[1:])
        if not is_prime(int(n_str[1:])):
            return False
        n_str = str(n)
        n = int(n_str[:-1])
        if not is_prime(int(n_str[:-1])):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(nums):
    x = nums[69]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)