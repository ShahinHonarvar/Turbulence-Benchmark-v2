def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[65]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            n = num
            is_truncatable = True
            while n > 9:
                n //= 10
                if not is_prime(n):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)