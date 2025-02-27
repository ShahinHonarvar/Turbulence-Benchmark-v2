def find_n_th_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_numbers = numbers[5:10]
    sub_numbers.sort()
    return sub_numbers[4]