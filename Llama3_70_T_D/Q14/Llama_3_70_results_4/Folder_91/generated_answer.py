def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = min(nums[:6])
    nums = [num for num in nums if num != smallest]
    if len(nums) < 1:
        return None
    second_smallest = min(nums[:6])
    return second_smallest