def find_second_largest_num(numbers):
    if len(numbers) < 65:
        return None
    target_range = numbers[14:65]
    if len(target_range) < 2:
        return None
    unique_nums = set(target_range)
    if len(unique_nums) < 2:
        return None
    return sorted(unique_nums)[-2]