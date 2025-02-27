def all_ints_div_by_num(nums):
    result = [num for num in nums[14:57] if num % -59 == 0]
    return result if result else []