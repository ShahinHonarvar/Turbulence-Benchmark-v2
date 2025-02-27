def all_left_right_truncatable_prime(nums):
    x = nums[28]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            is_truncatable = True
            temp = str(num)
            while len(temp) > 1:
                temp = temp[1:]
                if not is_prime(int(temp)):
                    is_truncatable = False
                    break
                temp = temp[:-1]
                if not is_prime(int(temp)):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True