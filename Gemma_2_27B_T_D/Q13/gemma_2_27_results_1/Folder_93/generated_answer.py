def find_second_largest_num(nums):
    if len(nums) >= 20 and all((nums[i] != nums[j] for i in range(75, 95) for j in range(i + 1, 95))):
        return sorted(nums[75:95])[-2]
    else:
        return None