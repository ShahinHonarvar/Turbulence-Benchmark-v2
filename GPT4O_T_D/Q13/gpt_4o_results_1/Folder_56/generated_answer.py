def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    sorted_nums = sorted(numbers, reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None