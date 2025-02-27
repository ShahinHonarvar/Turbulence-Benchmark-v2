def all_odd_ints_inclusive(nums):
    odd_nums_in_range = [num for num in nums if num % 2 != 0 and 19 <= num <= 92]
    if not odd_nums_in_range:
        return []
    return odd_nums_in_range