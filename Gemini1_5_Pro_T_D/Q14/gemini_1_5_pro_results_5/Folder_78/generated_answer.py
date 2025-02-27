def find_second_smallest_num(numbers):
    if len(numbers) < 79:
        return None
    sub_list = numbers[17:79]
    if len(set(sub_list)) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[1]