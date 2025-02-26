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
            is_truncatable = True
            test_num = num
            while len(str(test_num)) > 1:
                test_num = int(str(test_num)[1:])
                if not is_prime(test_num):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                result.append(num)
    return result