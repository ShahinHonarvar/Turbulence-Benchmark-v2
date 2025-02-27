def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    else:
        smallest = min(nums[0], nums[1], nums[2])
        nums.remove(smallest)
        return min(nums)