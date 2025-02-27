def find_smallest_num(nums):
    if len(nums) < 201:
        return None
    smallest = nums[30]
    for i in range(31, 201):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest