def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    smallest = min(nums[:3])
    second_smallest = min((i for i in nums[:3] if i != smallest))
    return second_smallest