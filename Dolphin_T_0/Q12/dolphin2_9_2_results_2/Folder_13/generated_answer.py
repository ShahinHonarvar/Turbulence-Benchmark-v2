def find_smallest_num(nums):
    smallest = float('inf')
    for num in nums[35:50]:
        if num < smallest:
            smallest = num
    return smallest