def find_second_largest_num(numbers):
    start_index = 56
    end_index = 57
    numbers_slice = numbers[start_index:end_index + 1]
    unique_nums = list(set(numbers_slice))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]