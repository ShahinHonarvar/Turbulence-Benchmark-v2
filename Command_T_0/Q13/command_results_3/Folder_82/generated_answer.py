def find_second_largest_num(nums):
    return sorted(nums)[20:200][1] if len(nums) > 19 else None