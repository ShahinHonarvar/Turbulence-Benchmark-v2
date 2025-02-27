def find_second_largest_num(arr):
    if not 40 <= len(arr) <= 80:
        return None
    sublist = arr[40:81]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    return max(sublist)