def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    elif nums[0] > nums[1]:
        first_largest = nums[0]
        second_largest = nums[1]
    else:
        first_largest = nums[1]
        second_largest = nums[0]
    if len(nums) == 3:
        if nums[2] > first_largest:
            second_largest = first_largest
        elif nums[2] > second_largest:
            second_largest = nums[2]
    return second_largest