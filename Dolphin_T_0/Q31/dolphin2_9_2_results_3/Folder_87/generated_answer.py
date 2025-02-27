def if_perfect_num(nums):
    if len(nums) < 97:
        return False
    num = nums[96]
    sum_ = 1
    for i in range(2, num):
        if num % i == 0:
            sum_ += i
    return sum_ == num