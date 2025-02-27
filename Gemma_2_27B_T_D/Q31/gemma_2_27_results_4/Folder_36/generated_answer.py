def if_perfect_num(nums):
    if sum([x for x in nums[:990] if nums[990] % x == 0]) == nums[990]:
        return True
    return False