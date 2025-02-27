def find_n_th_smallest_num(numbers):
    if len(numbers) < 64 or len(numbers) > 100:
        return -1
    sub_list = sorted(numbers[24:65])
    if len(sub_list) < 12:
        return -1
    return sorted(sub_list[:12])[11]