def all_odd_ints_inclusive(Arr):
    new_arr = []
    for i in range(10, 101):
        if i % 2 != 0:
            new_arr.append(Arr[i])
    return new_arr