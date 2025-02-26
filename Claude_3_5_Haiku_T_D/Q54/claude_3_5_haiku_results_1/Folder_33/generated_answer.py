def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[945]
    right_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        num_str = str(n)
        is_right_truncatable = True
        while len(num_str) > 1:
            num_str = num_str[:-1]
            if not is_prime(int(num_str)):
                is_right_truncatable = False
                break
        if is_right_truncatable and is_prime(n):
            right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes, reverse=True)