def find_n_th_smallest_num(numbers):
    n = 16
    if len(numbers[11:44]) < n:
        return -1
    numbers.sort()
    return numbers[11 + n - 1]