def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[73]
    left_right_truncatable_primes = []
    for i in range(11, x + 1):
        if '0' not in str(i) and is_prime(i):
            temp = str(i)
            truncatable = True
            for j in range(1, len(temp)):
                if not is_prime(int(temp[j:])) or not is_prime(int(temp[:-j])):
                    truncatable = False
                    break
            if truncatable:
                left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)