def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[77]
    truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            is_left_truncatable = True
            current = num
            while current > 0:
                if not is_prime(current):
                    is_left_truncatable = False
                    break
                current = int(str(current)[1:]) if len(str(current)) > 1 else 0
            if is_left_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)