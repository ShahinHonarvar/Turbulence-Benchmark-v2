def find_smallest_num(nums):
    smallest = nums[56]
    for num in nums[56:83]:
        if num < smallest:
            smallest = num
    return smallest