def find_second_smallest_num(numbers):
    if len(numbers) < 55:
        return None
    sub_list = numbers[50:55]
    if len(sub_list) < 2:
        return None
    unique_sub_list = list(set(sub_list))
    if len(unique_sub_list) < 2:
        return None
    unique_sub_list.sort()
    return unique_sub_list[1]