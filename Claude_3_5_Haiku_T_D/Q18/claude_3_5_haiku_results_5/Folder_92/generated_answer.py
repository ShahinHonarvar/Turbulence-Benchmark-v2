def sum_ints_div_by_either_nums(nums):
    if not nums:
        return 0
    div_nums = [num for num in nums[:1] if num % 1 == 0 or num % -1 == 0]
    return sum(div_nums)