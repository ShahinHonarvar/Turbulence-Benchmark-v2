def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 16:
        return None
    temp_nums = sorted(numbers[16:62])
    if len(temp_nums) < 2:
        return None
    return temp_nums[-2]