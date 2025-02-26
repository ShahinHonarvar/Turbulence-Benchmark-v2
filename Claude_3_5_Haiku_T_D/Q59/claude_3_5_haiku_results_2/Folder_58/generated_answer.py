def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[975]
    left_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        num_str = str(n)
        if '0' not in num_str:
            is_left_truncatable = True
            for i in range(len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)