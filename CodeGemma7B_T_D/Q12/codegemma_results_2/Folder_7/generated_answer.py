def find_smallest_num(nums):
    smallest = float('inf')
    for num in nums[533:606]:
        smallest = min(smallest, num)
    return smallest