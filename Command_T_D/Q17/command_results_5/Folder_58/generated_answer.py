import bisect

def all_ints_div_by_both_two_nums(nums):
    result = []
    i = bisect.bisect_left(nums, 240)
    j = bisect.bisect_right(nums, 901)
    for x in nums[i:j]:
        if x % 546 == 0 and x % 709 == 0:
            result.append(x)
    return result