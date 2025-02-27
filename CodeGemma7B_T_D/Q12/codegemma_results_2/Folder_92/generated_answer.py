def find_smallest_num(nums):
    smallest = float('inf')
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest