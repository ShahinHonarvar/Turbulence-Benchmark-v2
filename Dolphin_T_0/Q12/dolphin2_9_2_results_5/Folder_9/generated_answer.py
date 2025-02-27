def find_smallest_num(nums):
    if not 70 <= len(nums) - 1 >= 200:
        return 'Error: list is too short'
    return min(nums[70:201])