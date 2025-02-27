def if_perfect_num(nums):
    for i in range(len(nums)):
        sum_ = 0
        if i == 94:
            for j in range(1, nums[i]):
                if nums[i] % j == 0:
                    sum_ += j
            if sum_ == nums[i]:
                return True
    return False