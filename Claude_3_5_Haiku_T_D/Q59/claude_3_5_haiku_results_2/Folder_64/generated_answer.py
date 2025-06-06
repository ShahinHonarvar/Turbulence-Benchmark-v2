def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[4]
    result = []
    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            temp_num = num
            while len(str(temp_num)) > 1:
                temp_num = int(str(temp_num)[1:])
                if not is_prime(temp_num):
                    truncatable = False
                    break
            if truncatable and is_prime(num):
                result.append(num)
    return sorted(result)