def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 10:
        return None
    return sorted(nums)[1]