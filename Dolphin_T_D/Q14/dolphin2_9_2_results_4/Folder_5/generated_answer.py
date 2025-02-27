def find_second_smallest_num(numbers):
    sublist = numbers[3:6]
    if len(set(sublist)) < 2:
        return None
    else:
        sorted_nums = sorted(sublist)
        return sorted_nums[1]