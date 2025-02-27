def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) < 401:
        return None
    min_num1 = min(nums[310:371])
    nums = [num for num in nums if num > min_num1]
    if len(nums) == 0:
        return None
    min_num2 = min(nums[310:371])
    return min_num2