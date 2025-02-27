def find_second_smallest_num(numbers):
    if len(numbers) > 88 and len(numbers[75:89]) > 1:
        sorted_nums = sorted(numbers[75:89])
        return sorted_nums[1]
    else:
        return None