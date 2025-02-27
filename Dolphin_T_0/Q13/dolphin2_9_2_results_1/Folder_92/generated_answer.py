def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 2:
        return None
    max_num = max(numbers)
    new_list = [num for num in numbers if num != max_num]
    if len(new_list) < 2:
        return None
    return max(new_list)