def find_smallest_num(nums):
    small = float('inf')
    for num in nums[36:47]:
        if num < small:
            small = num
    return small