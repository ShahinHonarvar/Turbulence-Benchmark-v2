def find_second_largest_num(numbers):
    if len(numbers) < 92:
        return None
    sublist = numbers[91:100]
    if len(sublist) < 2:
        return None
    unique_nums = sorted(set(sublist), reverse=True)
    return unique_nums[1] if len(unique_nums) >= 2 else None