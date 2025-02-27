def find_smallest_num(nums):
    smallest = float('inf')
    for i in range(29, 80):
        smallest = min(smallest, nums[i])
    return smallest