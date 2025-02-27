def find_n_th_smallest_num(numbers):
    if not isinstance(numbers, list) or len(numbers) < 19 or len(numbers) < 53:
        return None
    sublist = numbers[11:54]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[18]