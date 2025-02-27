def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    sub_list = numbers[200:201]
    if len(set(sub_list)) != len(sub_list):
        return None
    if len(sub_list) == 1:
        return None
    else:
        sorted_list = sorted(sub_list)
        return sorted_list[-2]