def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = numbers[4:5]
    if len(set(sub_list)) != len(sub_list):
        return None
    if len(sub_list) == 1:
        return sub_list[0]
    else:
        return sorted(sub_list)[1]