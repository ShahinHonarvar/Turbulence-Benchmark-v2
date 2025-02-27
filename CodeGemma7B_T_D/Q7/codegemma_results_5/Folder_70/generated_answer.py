def all_even_ints_inclusive(nums):
    nums_in_range = []
    for num in nums[28:33]:
        if num % 2 == 0:
            nums_in_range.append(num)
    return nums_in_range