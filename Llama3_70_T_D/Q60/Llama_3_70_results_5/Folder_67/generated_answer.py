def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[71]
    primes = []
    for num in range(11, x + 1):
        if '0' not in str(num):
            truncatable = True
            left = str(num)
            right = str(num)
            while len(left) > 1:
                left = left[1:]
                right = right[:-1]
                if not is_prime(int(left)) or not is_prime(int(right)):
                    truncatable = False
                    break
            if truncatable and is_prime(num):
                primes.append(num)
    primes.sort(reverse=True)
    return primes