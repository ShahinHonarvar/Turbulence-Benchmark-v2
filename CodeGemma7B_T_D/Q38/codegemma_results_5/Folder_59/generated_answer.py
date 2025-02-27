def find_subset_of_length_n(arr):
    list = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            list.append((arr[i], arr[j]))
    return len(list)