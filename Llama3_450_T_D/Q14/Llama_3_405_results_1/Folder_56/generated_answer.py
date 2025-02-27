def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = min(nums)
    second_smallest = min((num for num in nums if num != smallest))
    return second_smallest if second_smallest != smallest else None