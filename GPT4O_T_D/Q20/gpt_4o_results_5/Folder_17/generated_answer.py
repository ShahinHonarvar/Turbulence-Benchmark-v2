def find_n_th_smallest_num(numbers):
    if len(numbers) < 86:
        return None
    sub_list = numbers[69:86]
    sub_list.sort()
    return sub_list[6]