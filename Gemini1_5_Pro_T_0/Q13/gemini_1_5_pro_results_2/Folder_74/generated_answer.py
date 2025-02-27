def find_second_largest_num(numbers):
    if len(numbers) < 79 or 17 >= len(numbers):
        return None
    sliced_list = numbers[17:79]
    if len(set(sliced_list)) < 2:
        return None
    largest_num = max(sliced_list)
    sliced_list.remove(largest_num)
    return max(sliced_list)