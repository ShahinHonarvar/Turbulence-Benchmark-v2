def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers)
    try:
        return sorted_nums[262:747][-2]
    except IndexError:
        return 'None'