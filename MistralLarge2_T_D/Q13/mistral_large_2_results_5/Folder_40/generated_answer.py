def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    first_largest = max(nums[:3])
    nums.remove(first_largest)
    second_largest = max(nums[:2])
    return second_largest