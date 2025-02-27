def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[43]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            if is_prime(num):
                temp = str(num)
                while len(temp) > 1:
                    temp = temp[1:]
                    if not is_prime(int(temp)):
                        break
                else:
                    left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)