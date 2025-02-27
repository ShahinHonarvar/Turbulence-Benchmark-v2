def find_second_largest_num(list_of_nums):
    if 538 >= len(list_of_nums) or 527 < 0:
        return None
    valid_nums = list_of_nums[527:539]
    if len(set(valid_nums)) < 2:
        return None
    else:
        sorted_nums = sorted(set(valid_nums))
        return sorted_nums[-2]