def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:28]) + 1)][-2]