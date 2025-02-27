def lists_with_product_equal_n(arr):
    n = len(arr)
    arr = arr + arr
    start = 0
    result = []
    for end in range(n, 2 * n):
        while start < end and arr[start] * arr[end] > 18:
            start += 1
        while start < end and arr[start] * arr[end] < 18:
            end -= 1
        if start < end and arr[start] * arr[end] == 18:
            result.append(arr[start:end + 1])
    return result