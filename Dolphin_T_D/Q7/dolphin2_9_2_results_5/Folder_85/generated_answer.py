def all_even_ints_inclusive(arr):
    even_ints = []
    for i in range(6, 9):
        if i < len(arr):
            if arr[i] % 2 == 0:
                even_ints.append(arr[i])
    return even_ints