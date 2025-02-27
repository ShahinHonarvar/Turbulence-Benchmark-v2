def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    sub_list = numbers[26:53]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]