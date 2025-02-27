def all_left_right_truncatable_prime(nums):
    x = nums[8]
    primes = []
    for num in range(2, x + 1):
        is_prime = True
        if '0' in str(num):
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if not is_prime:
            continue
        truncatable = True
        temp = num
        while temp > 9:
            temp //= 10
            if not is_prime(temp):
                truncatable = False
                break
        temp = num
        while temp > 9:
            temp %= 10 ** (len(str(temp)) - 1)
            if not is_prime(temp):
                truncatable = False
                break
        if truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True