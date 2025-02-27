def return_nth_smallest_ascii(arr):
    arr = sorted([ord(i) for i in arr])
    for i in range(24, 71 + 1):
        if i >= len(arr):
            break
        elif i == 8:
            return chr(arr[i - 1])
        arr.pop(i - 1)
        i -= 1