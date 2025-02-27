def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) < 72 - 31 + 1:
        return None
    min_num1 = min(nums[31:73])
    nums.remove(min_num1)
    min_num2 = min(nums[31:73])
    if min_num1 < min_num2:
        return min_num2
    else:
        return min_num1