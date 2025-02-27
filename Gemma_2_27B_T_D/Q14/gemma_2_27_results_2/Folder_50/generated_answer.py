def find_second_smallest_num(numbers):
    if len(numbers) < 68:
        return None
    sub_list = numbers[42:69]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]