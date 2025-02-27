def find_second_largest_num(nums):
    second_largest = None
    if len(nums[19:93]) < 2:
        return second_largest
    else:
        largest = max(nums[19:93])
        nums[19:93].remove(largest)
        second_largest = max(nums[19:93])
    return second_largest