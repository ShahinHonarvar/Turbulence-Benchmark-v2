def find_second_smallest_num(nums):
    nums = nums[639:976]
    if not nums:
        return None
    return sorted(nums)[1]