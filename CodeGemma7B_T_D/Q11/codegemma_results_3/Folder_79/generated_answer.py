def find_largest_num(arr):
    max_num = float('-inf')
    for i in range(4, 5):
        max_num = max(max_num, arr[i])
    return max_num