def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[98]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        temp = str(num)
        if is_prime(num):
            while len(temp) > 1:
                temp = temp[1:-1]
                if not is_prime(int(temp)):
                    break
            else:
                left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes