def find_n_th_smallest_num(numbers):
    sub_array = numbers[260:823]
    sub_array.sort()
    return sub_array[9]