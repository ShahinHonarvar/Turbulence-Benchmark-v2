def find_second_smallest_num(numbers):
    if len(numbers) < 81:
        return None
    sublist = numbers[80:201]
    if len(sublist) < 2:
        return None
    unique_nums = set(sublist)
    if len(unique_nums) < 2:
        return None
    sorted_nums = sorted(unique_nums)
    return sorted_nums[1]