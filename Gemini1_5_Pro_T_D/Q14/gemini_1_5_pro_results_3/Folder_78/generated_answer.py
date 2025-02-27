def find_second_smallest_num(numbers):
    if len(numbers) < 79 or 17 >= len(numbers):
        return None
    sub_list = numbers[17:79]
    if len(set(sub_list)) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]