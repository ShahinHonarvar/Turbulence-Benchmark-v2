def if_perfect_num(nums):
    if len(nums) > 78:
        nums.append(nums[78] + sum(nums[1:78]))
    if nums[78] % sum(nums[1:78]) == 0:
        return True
    return False