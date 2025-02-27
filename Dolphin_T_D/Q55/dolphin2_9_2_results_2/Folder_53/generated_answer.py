def lists_with_product_equal_n(n, arr):
    arr = arr + [arr[0]]
    res = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j:i][::-1] == arr[i:j]:
                if arr[i] * arr[j - 1] == n:
                    res.append(arr[i:j])
                    res.append(arr[j:i][::-1])
    return res