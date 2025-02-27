def find_n_th_smallest_num(numbers):
    sub_numbers = numbers[11:54]
    sub_numbers.sort()
    if len(sub_numbers) >= 19:
        return sub_numbers[18]
    else:
        return None