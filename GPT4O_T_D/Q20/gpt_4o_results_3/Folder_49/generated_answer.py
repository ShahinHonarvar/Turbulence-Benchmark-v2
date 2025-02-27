def find_n_th_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    sub_list = numbers[20:201]
    sub_list.sort()
    if len(sub_list) < 11:
        return None
    return sub_list[10]