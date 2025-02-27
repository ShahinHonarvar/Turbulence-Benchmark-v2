def all_left_truncatable_prime(nums):
    x = nums[177]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            is_left_truncatable = True
            num_str = str(i)
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True