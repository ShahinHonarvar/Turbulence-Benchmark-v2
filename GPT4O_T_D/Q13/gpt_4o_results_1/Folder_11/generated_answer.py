def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    sublist = numbers[37:52]
    if len(sublist) < 2:
        return None
    unique_nums = list(set(sublist))
    unique_nums.sort(reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None