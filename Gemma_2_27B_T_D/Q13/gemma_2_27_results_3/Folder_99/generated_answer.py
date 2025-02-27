def find_second_largest_num(nums):
    if len(nums) < 61 or any((nums[i] == nums[j] for i in range(310, 371) for j in range(i + 1, 371))):
        return None
    return sorted(nums[310:371])[-2]