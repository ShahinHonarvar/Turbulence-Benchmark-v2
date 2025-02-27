def find_n_th_smallest_num(arr):
    start = 10
    end = 100
    arr = arr[start:end + 1]
    return sorted(arr)[9]