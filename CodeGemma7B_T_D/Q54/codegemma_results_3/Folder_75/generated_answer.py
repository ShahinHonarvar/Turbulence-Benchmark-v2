def all_right_truncatable_prime(nums):
    n = nums[41]
    right_truncatable_primes = []
    for i in range(2, n):
        if is_prime(i):
            temp = str(i)
            for j in range(1, len(temp)):
                if not is_prime(int(temp[:-j])):
                    break
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True