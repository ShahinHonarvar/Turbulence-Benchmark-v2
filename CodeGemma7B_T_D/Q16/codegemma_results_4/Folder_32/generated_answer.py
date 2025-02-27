def sum_even_ints_inclusive(nums):
    nums_sum = 0
    for num in nums[21:98]:
        if num % 2 == 0:
            nums_sum += num
    if nums_sum == 0:
        return 0
    else:
        return nums_sum