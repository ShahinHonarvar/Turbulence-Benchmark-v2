def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[70]
    truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            temp = str(num)
            is_truncatable = True
            while len(temp) > 0:
                if not is_prime(int(temp)):
                    is_truncatable = False
                    break
                temp = temp[1:]
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)