def find_second_smallest_num(nums):
    if len(nums) < 55 or any((nums[i] == nums[j] for i in range(50, 55) for j in range(i + 1, 55))):
        return None
    return sorted(nums[50:55])[1]