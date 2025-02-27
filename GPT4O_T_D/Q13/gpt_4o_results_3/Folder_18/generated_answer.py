def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    sub_list = numbers[35:50]
    if len(sub_list) < 2:
        return None
    max_num = max(sub_list)
    sub_list.remove(max_num)
    second_max = max(sub_list)
    return second_max