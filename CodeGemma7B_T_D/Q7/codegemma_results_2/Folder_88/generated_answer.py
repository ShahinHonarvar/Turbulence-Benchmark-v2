def all_even_ints_inclusive(nums):
    range_start = 4
    range_end = 8
    result = []
    for i in range(range_start, range_end + 1):
        if i >= len(nums) or nums[i] % 2 != 0:
            continue
        result.append(nums[i])
    return result