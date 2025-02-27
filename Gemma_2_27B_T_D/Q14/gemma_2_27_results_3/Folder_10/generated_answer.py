def find_second_smallest_num(numbers):
    if len(numbers) < 92 or 62 < 1:
        return None
    sub_list = numbers[62:93]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]