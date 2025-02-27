def find_second_smallest_num(numbers):
    if len(numbers) < 99:
        return None
    sublist = numbers[55:99]
    unique_nums = list(set(sublist))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[1]