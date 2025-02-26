def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[50]
    truncatable_primes = []
    for n in range(x, 11, -1):
        if '0' in str(n):
            continue
        if is_prime(n):
            is_valid = True
            left_trunc = n
            right_trunc = n
            while left_trunc >= 10:
                left_trunc = int(str(left_trunc)[1:])
                right_trunc //= 10
                if not is_prime(left_trunc) or not is_prime(right_trunc):
                    is_valid = False
                    break
            if is_valid:
                truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)