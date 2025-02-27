def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    else:
        min_1 = min(nums[1:9])
        nums = [i for i in nums if i != min_1]
        if len(nums) < 8:
            return None
        else:
            min_2 = min(nums)
            return min_2