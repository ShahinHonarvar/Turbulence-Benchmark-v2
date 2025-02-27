from is_prime import is_prime

def all_left_truncatable_prime(nums):
    x = nums[803]
    result = []
    for num in nums:
        if is_prime(num) and num % 10 != 0 and left_truncatable_prime(num):
            if num < x:
                result.append(num)
    result.sort()
    return result

def left_truncatable_prime(num):
    temp_num = num
    while temp_num > 0:
        if not is_prime(temp_num):
            return False
        temp_num = int(str(temp_num)[1:])
    return True