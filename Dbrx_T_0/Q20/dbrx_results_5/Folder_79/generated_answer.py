def find_n_th_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sub_numbers = numbers[4:8]
    sub_numbers.sort()
    return sub_numbers[3]