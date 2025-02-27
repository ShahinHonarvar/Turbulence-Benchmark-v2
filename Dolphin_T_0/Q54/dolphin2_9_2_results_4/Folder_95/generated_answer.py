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

def all_right_truncatable_prime(nums):
    x = nums[77]
    primes = [x for x in range(2, x) if is_prime(x)]
    right_truncatable_primes = [p for p in primes if all((is_prime(int(str(p)[i:])) for i in range(len(str(p)) - 1))) and len(str(p)) > 1]
    return sorted(right_truncatable_primes)