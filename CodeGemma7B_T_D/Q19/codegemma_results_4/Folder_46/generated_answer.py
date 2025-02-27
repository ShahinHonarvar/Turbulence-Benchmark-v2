def all_ints_not_div_by_num(nums):
    for num in nums[18:60]:
        if num % 86 != 0:
            yield from num