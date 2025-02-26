def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[43]
    truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            is_left_truncatable = True
            current_num = num
            while len(str(current_num)) > 1:
                current_num = int(str(current_num)[1:])
                if not is_prime(current_num):
                    is_left_truncatable = False
                    break
            if is_left_truncatable and is_prime(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)