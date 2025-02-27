def gcf_three_nums(nums):
    first = nums[13]
    second = nums[70]
    third = nums[32]
    if second > first:
        first, second = (second, first)
    if third > second:
        second, third = (third, second)
    while second != 0:
        first, second = (second, first % second)
    return first