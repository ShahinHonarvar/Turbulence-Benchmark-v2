def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) <= 20 or len(nums) <= 30:
        return None
    else:
        return nums[20:31][::-1][1]