def find_second_smallest_num(numbers):
    if len(numbers) < 79 or 17 >= len(numbers):
        return None
    sliced_numbers = numbers[17:79]
    if len(set(sliced_numbers)) < 2:
        return None
    sorted_nums = sorted(sliced_numbers)
    return sorted_nums[1]