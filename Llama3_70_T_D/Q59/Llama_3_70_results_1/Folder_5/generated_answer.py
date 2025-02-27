def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[55]
    left_truncatable_primes = set()
    for num in range(2, x):
        if '0' in str(num):
            continue
        temp = str(num)
        if is_prime(int(temp)):
            while len(temp) > 1:
                temp = temp[1:]
                if not is_prime(int(temp)):
                    break
            else:
                left_truncatable_primes.add(num)
    return sorted(list(left_truncatable_primes))