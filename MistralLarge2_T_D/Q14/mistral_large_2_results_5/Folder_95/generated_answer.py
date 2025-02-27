def find_second_smallest_num(numbers):
    if len(numbers) <= 85:
        return None
    sublist = numbers[75:86]
    if len(sublist) < 2:
        return None
    unique_nums = list(set(sublist))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[1]