def find_second_smallest_num(nums):
    if len(nums) < 687 or len(nums) > 987:
        return None
    nums.sort()
    return nums[686] if len(nums) > 686 else None