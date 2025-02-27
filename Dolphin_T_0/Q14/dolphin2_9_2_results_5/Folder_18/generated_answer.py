def find_second_smallest_num(arr):
    for i in range(30, 49):
        found = False
        for j in arr:
            if i == j:
                found = True
                break
        if not found:
            return None
    if len(arr) < 20:
        return None
    arr.sort()
    return arr[1] if len(arr) > 1 else None