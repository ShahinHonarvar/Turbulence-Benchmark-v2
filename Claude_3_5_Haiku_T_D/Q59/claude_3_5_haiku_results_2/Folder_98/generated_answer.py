def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[8]
    result = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            is_left_truncatable = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    is_left_truncatable = False
                    break
                temp //= 10
            if is_left_truncatable:
                result.append(num)
    return sorted(result, reverse=True)