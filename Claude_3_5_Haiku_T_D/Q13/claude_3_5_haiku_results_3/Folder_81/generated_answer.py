def find_second_largest_num(numbers):
    if len(numbers) < 11:
        return None
    sublist = numbers[10:101]
    if len(sublist) == 0:
        return None
    unique_nums = sorted(set(sublist), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None