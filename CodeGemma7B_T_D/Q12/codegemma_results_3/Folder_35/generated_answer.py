def find_smallest_num(nums):
    smallest = nums[43]
    for num in nums[43:87]:
        if num < smallest:
            smallest = num
    return smallest