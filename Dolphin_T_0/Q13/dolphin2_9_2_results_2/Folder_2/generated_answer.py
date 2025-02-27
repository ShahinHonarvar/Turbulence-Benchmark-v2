def find_second_largest_num(nums):
    try:
        subset = nums[15:40]
        subset.sort(reverse=True)
        return subset[1]
    except IndexError:
        return None