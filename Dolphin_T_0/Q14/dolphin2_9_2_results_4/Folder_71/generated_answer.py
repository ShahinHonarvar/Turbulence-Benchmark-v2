def find_second_smallest_num(arr):
    if len(arr) < 52:
        return None
    else:
        while True:
            sub_arr = arr[29:52]
            smallest = min(sub_arr)
            sub_arr.remove(smallest)
            if len(sub_arr) == 0:
                return None
            second_smallest = min(sub_arr)
            if second_smallest != smallest:
                return second_smallest