def find_second_smallest_num(numbers):
    if len(numbers) < 200:
        return None
    sub_list = numbers[50:201]
    if len(sub_list) == 1:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]