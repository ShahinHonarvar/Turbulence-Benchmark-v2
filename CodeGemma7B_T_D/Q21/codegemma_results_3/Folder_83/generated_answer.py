def all_ints_div_by_num(nums):
    result = [num for num in nums[40:401] if num % 7 == 0]
    return result or []