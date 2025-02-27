def composite_nums_between_indices(nums):
    range_start, range_end = (13 + 1, 68 + 1)
    composite_nums = set(filter(lambda x: not isinstance(x, int) or (x % 1 == 0 and x != 1), nums[range_start:range_end]))
    return composite_nums if composite_nums else set()