def if_perfect_num(nums):
    num = nums[126]
    if int(num ** 0.5) == num ** 0.5:
        return True
    return False