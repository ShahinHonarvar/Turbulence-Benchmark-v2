def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[57]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            is_truncatable = True
            num_str = str(i)
            while len(num_str) > 1:
                num_str = num_str[1:]
                if not is_prime(int(num_str)):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(i):
                primes.append(i)
    return sorted(primes, reverse=True)