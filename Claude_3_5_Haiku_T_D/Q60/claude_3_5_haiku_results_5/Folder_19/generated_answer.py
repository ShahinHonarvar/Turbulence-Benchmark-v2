def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[67]
    truncatable_primes = []
    for n in range(x, 11, -1):
        if '0' in str(n):
            continue
        is_truncatable = True
        num_str = str(n)
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not is_prime(int(num_str)):
                is_truncatable = False
                break
        num_str = str(n)
        while len(num_str) > 1:
            num_str = num_str[:-1]
            if not is_prime(int(num_str)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)