def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = set(numbers[4:9])
    if len(sub_list) < 2:
        return None
    smallest_num = min(sub_list)
    sub_list.remove(smallest_num)
    second_smallest_num = min(sub_list)
    return second_smallest_num