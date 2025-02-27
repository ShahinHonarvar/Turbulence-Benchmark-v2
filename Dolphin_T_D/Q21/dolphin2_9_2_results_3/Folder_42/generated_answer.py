def all_ints_div_by_num(nums):
    result = [num for num in nums[31:93] if num % 20 == 0]
    return result if result else []