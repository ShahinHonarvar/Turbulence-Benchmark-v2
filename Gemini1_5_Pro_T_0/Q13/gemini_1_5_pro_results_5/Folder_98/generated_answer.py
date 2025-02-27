def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 7:
        return None
    unique_nums = set(numbers[:7])
    if len(unique_nums) < 2:
        return None
    sorted_nums = sorted(unique_nums)
    return sorted_nums[-2]