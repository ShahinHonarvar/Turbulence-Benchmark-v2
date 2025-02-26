def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[70]
    result = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            truncatable = True
            test_num = num
            while test_num > 0:
                if not is_prime(test_num):
                    truncatable = False
                    break
                test_num //= 10
            if truncatable:
                result.append(num)
    return sorted(result, reverse=True)