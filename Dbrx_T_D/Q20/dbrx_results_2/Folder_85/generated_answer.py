def find_n_th_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sub_numbers = numbers[2:9]
    sub_numbers.sort()
    if len(sub_numbers) < 5:
        return None
    return sub_numbers[4]