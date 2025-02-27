def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 9:
        return None
    second_smallest = min([num for num in nums if num != min(nums)])
    return second_smallest