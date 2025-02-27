def all_ints_div_by_num(nums):
    lst = [num for num in nums[0:3] if num % -8 == 0]
    return lst if lst else []