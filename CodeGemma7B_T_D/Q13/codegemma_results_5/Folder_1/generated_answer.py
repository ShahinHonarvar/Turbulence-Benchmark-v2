def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 2:
        return None
    sorted_nums = sorted(numbers, reverse=True)
    if len(sorted_nums) <= 31:
        return sorted_nums[0]
    else:
        return sorted_nums[31]