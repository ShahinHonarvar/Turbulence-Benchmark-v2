def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = max(nums[:6])
    nums.remove(largest)
    return max(nums[:6])