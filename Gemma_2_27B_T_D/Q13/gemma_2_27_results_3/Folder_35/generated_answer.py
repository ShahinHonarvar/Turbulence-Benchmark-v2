def find_second_largest_num(nums):
    if len(nums) < 19 or any((nums[i] == nums[j] for i in range(30, 49) for j in range(i + 1, 49))):
        return None
    return sorted(nums[30:49])[-2]