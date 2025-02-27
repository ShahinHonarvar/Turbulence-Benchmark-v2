def find_smallest_num(nums):
    smallest = float('inf')
    for num in nums[1:9]:
        if num < smallest:
            smallest = num
    return smallest