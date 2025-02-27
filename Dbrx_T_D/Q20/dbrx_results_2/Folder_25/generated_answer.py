def find_n_th_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    sub_list = numbers[13:41]
    sub_list.sort()
    return sub_list[4]