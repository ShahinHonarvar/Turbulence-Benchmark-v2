def all_pos_ints_inclusive(arr):
    numbers = []
    for i in range(52, len(arr)):
        if arr[i] >= 1:
            numbers.append(arr[i])
    return numbers