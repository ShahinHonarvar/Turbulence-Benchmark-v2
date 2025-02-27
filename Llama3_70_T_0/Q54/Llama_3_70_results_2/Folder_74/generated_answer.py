def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[36]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = str(num)
            while len(temp) > 1:
                temp = temp[:-1]
                if not is_prime(int(temp)):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)