def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_two = nums[0:2]
    if first_two[0] > first_two[1]:
        return first_two[1]
    else:
        return first_two[0]