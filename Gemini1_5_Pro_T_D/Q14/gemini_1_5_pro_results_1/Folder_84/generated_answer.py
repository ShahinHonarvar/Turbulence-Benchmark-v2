def find_second_smallest_num(numbers):
    if len(numbers) < 81:
        return None
    sub_list = numbers[40:81]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[1]