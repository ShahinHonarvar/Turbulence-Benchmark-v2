def find_n_th_smallest_num(numbers):
    if len(numbers) < 98:
        return 'Input list is too short.'
    sub_list = numbers[29:99]
    sub_list.sort()
    return sub_list[4]