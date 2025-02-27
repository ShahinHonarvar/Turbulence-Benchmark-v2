def find_second_smallest_num(nums):
    try:
        nums = nums[5:8]
        nums.remove(min(nums))
        return min(nums)
    except:
        return 'None'