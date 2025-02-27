def all_odd_ints_exclusive(arr):
    odd_nums = []
    for i in range(1, len(arr) - 1):
        if arr[i] % 2 != 0:
            odd_nums.append(arr[i])
    return odd_nums