def find_n_th_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sub_list = numbers[2:9]
    sub_list.sort()
    return sub_list[6]