def find_second_smallest_num(nums):
    nums.sort()
    for i in range(40, 201):
        if i < len(nums):
            if len(nums) > i + 1:
                return nums[i + 1]
        else:
            return None