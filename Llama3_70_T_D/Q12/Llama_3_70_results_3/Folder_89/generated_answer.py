def find_smallest_num(nums):
    smallest = nums[22]
    for num in nums[23:51]:
        if num < smallest:
            smallest = num
    return smallest