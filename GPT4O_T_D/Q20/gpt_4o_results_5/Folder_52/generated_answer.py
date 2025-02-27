def find_n_th_smallest_num(numbers):
    segment = numbers[40:76]
    segment.sort()
    return segment[18]