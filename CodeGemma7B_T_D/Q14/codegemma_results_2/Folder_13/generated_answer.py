def find_second_smallest_num(nums):
    if len(nums) < 30 or nums[28] > nums[32]:
        return None
    second_smallest = float('inf')
    for i in range(28, 33):
        if nums[i] < second_smallest and nums[i] != nums[28]:
            second_smallest = nums[i]
    return second_smallest