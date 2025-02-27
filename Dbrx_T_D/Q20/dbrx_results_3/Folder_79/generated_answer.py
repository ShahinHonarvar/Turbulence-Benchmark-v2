def find_n_th_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sub_list = numbers[4:8]
    sub_list.sort()
    return sub_list[3]