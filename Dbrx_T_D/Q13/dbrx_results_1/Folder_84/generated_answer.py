def find_second_largest_num(numbers):
    unique_nums = list(set(numbers[43:87]))
    unique_nums.sort(reverse=True)
    if len(unique_nums) < 2:
        return None
    else:
        return unique_nums[1]