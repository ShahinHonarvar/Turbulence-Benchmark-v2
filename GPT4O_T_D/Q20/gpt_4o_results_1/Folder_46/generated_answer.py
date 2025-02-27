def find_n_th_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    sub_list = numbers[36:94]
    sub_list.sort()
    return sub_list[3]