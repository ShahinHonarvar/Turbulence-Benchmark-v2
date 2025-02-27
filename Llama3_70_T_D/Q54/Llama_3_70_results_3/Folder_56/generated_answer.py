def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[30]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            num_str = str(i)
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[:-j])):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)