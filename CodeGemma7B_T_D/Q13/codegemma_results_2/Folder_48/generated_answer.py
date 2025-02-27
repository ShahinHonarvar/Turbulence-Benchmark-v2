def find_second_largest_num(list_of_numbers):
    sorted_nums = sorted(list_of_numbers[533:606], reverse=True)
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    return None