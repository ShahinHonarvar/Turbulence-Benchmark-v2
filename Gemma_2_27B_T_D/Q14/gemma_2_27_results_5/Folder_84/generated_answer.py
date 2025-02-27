def find_second_smallest_num(nums):
    if len(nums) < 81 or len(nums) < 41:
        return None
    second_smallest = min(nums[40:81])
    nums.remove(second_smallest)
    return min(nums[40:81])