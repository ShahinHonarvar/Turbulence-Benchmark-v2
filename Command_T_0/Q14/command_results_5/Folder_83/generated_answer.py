def find_second_smallest_num(nums):
    return sorted(nums)[90:200][1] if len(nums) > 90 and len(nums) > 200 else None