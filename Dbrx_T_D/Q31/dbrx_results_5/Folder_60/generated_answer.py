def if_perfect_num(nums):
    if len(nums) > 88:
        num = nums[88]
        return num > 0 and sum([x for x in range(1, num) if num % x == 0]) == num
    else:
        return False