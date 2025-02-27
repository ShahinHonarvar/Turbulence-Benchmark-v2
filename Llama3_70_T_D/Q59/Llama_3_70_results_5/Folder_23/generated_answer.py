def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[77]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        if not is_prime(i):
            continue
        temp = str(i)
        while len(temp) > 1:
            temp = temp[1:]
            if not is_prime(int(temp)):
                break
        else:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes