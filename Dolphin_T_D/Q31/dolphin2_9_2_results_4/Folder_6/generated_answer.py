def if_perfect_num(nums):
    if len(nums) > 790:
        seventh_num = nums[790]
        sum = 1
        for i in range(2, seventh_num):
            if seventh_num % i == 0:
                sum += i
        if sum == seventh_num:
            return True
    return False