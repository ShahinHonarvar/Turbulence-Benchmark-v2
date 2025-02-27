def if_perfect_num(nums):
    if len(nums) > 222:
        num = nums[222]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum = sum + i
        return sum == num
    else:
        return False