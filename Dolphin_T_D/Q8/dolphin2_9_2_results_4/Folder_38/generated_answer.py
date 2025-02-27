def all_even_ints_exclusive(arr):
    even_ints = []
    for i in range(15, 40):
        if i % 2 == 0:
            even_ints.append(arr[i])
    return even_ints