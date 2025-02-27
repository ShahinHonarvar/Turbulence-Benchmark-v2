def find_second_largest_num(nums):
    if len(nums) < 6 or nums[4] == nums[5]:
        return None
    second_largest = nums[3]
    idx = 4
    while idx <= 5:
        if nums[idx] > second_largest:
            second_largest = nums[idx]
        idx += 1
    return second_largest