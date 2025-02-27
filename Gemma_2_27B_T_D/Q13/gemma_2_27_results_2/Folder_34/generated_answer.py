def find_second_largest_num(nums):
    if len(nums) < 62 or any((nums[i] == nums[j] for i in range(16, 62) for j in range(i + 1, 62))):
        return None
    return sorted(nums[16:62])[::-1][1]