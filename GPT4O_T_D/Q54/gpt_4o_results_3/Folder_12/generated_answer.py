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

def right_truncatable(prime):
    if prime < 10:
        return is_prime(prime)
    return all((is_prime(int(str(prime)[:i])) for i in range(1, len(str(prime)) + 1)))

def all_right_truncatable_prime(nums):
    x = nums[70]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and right_truncatable(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)