def sum_ints_div_by_either_nums(nums):
    sum_list = sum([num for num in nums[80:201] if num % 10 == 0 or num % 1000 == 0])
    return sum_list or 0