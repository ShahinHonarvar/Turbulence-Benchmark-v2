def find_largest_num(arr):
    largest = float('-inf')
    for num in arr[30:88]:
        largest = max(largest, num)
    return largest