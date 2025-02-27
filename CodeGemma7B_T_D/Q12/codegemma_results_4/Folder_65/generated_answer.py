def find_smallest_num(nums):
    smallest = float('inf')
    for num in nums[12:93]:
        if num < smallest:
            smallest = num
    return smallest