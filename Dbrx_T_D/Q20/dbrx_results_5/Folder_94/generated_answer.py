def find_n_th_smallest_num(numbers):
    if len(numbers) < 70 or len(numbers) < 57:
        return None
    sub_list = numbers[57:71]
    sub_list.sort()
    return sub_list[5]