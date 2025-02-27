def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[70]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = str(num)
            while temp:
                if not is_prime(int(temp)):
                    break
                temp = temp[:-1]
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)