def sum_even_ints_inclusive(nums):
    start_index = 29
    end_index = 29
    sum = 0
    if len(nums) > end_index:
        for i in range(start_index, end_index + 1):
            if nums[i] % 2 == 0:
                sum += nums[i]
    return sum