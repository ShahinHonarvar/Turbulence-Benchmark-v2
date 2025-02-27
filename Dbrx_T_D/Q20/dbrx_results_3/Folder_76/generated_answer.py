def find_n_th_smallest_num(numbers):
    if len(numbers) < 823:
        return None
    sub_list = sorted(numbers[260:823])
    if len(sub_list) < 10:
        return None
    return sub_list[9]