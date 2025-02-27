def find_second_smallest_num(nums):
    if not nums[8:10]:
        return None
    return sorted(nums[8:10])[1]