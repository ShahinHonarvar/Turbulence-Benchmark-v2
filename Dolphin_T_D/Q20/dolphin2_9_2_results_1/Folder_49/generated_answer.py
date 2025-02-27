def find_n_th_smallest_num(lst):
    partition = lambda arr, low, high: arr[low]
    pivot = partition(lst, 20, 200)
    pivot_index = lst.index(pivot)
    if pivot_index == 10:
        return pivot
    elif pivot_index > 10:
        return find_n_th_smallest_num(lst[:pivot_index + 1])
    else:
        return find_n_th_smallest_num(lst[pivot_index:])