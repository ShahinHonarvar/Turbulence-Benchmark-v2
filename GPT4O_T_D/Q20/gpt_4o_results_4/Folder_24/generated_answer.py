def find_n_th_smallest_num(numbers):
    subrange = numbers[43:81]
    subrange.sort()
    return subrange[5]