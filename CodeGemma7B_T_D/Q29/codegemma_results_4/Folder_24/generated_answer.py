def gcf_two_nums(nums):
    first = nums[84]
    second = nums[21]
    while first != second:
        if first > second:
            first -= second
        else:
            second -= first
    return first