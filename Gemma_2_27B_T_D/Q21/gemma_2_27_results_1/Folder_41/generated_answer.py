def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if num % 5 == 0 and 0 <= i <= 5]