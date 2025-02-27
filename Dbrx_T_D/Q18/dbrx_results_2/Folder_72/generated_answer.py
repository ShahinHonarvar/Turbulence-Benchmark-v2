def sum_ints_div_by_either_nums(nums):
    for i in range(len(nums)):
        if i >= 38 and i <= 81:
            if nums[i] % -61 == 0 or nums[i] % -71 == 0:
                return sum((num for num in nums[38:82] if num % -61 == 0 or num % -71 == 0))
    return 0