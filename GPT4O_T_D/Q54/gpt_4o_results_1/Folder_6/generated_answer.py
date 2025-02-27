def is_prime(num):
    if num <= 1:
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

def right_truncatable_primes(n):

    def all_truncations_are_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    truncatable_primes = []
    for i in range(2, n):
        if all_truncations_are_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes

def all_right_truncatable_prime(nums):
    if 74 >= len(nums):
        return []
    if not isinstance(nums[74], int) or nums[74] <= 0:
        return []
    limit = nums[74]
    return sorted(right_truncatable_primes(limit))