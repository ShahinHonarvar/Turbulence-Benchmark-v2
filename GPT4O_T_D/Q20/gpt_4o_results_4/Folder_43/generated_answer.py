def find_n_th_smallest_num(numbers):
    if len(numbers) < 65:
        return None
    sub_list = numbers[28:65]
    sub_list.sort()
    if len(sub_list) < 16:
        return None
    return sub_list[15]