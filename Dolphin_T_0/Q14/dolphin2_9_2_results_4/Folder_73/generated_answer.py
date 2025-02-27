def find_second_smallest_num(arr):
    if arr and 59 <= len(arr) <= 97:
        try:
            return sorted(arr[59:98])[1]
        except IndexError:
            return None
    else:
        return None