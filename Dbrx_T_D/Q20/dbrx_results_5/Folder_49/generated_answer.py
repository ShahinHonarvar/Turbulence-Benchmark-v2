def find_n_th_smallest_num(numbers):
    sub_numbers = numbers[20:201]
    sub_numbers.sort()
    return sub_numbers[10]