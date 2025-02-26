def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[645]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        temp_num = num
        while len(str(temp_num)) > 1:
            temp_num = int(str(temp_num)[1:])
            if not is_prime(temp_num):
                is_truncatable = False
                break
        temp_num = num
        while len(str(temp_num)) > 1:
            temp_num = int(str(temp_num)[:-1])
            if not is_prime(temp_num):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            result.append(num)
    return sorted(result)