def all_left_truncatable_prime(nums):
    x = nums[50]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            is_left_truncatable = True
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True