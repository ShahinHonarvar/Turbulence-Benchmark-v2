def find_second_smallest_num(nums):
    if len(nums) <= 48 or min(nums) == max(nums):
        return None
    nums_slice = sorted(nums)[30:49]
    return nums_slice[1] if len(nums_slice) > 1 else None