def lists_with_product_equal_n(arr):
    result = []
    arr = arr + arr
    for y in range(len(arr)):
        for x in range(y + 1, len(arr)):
            if arr[x] == 1:
                continue
            product = 1
            for z in range(x, y + len(arr)):
                product *= arr[z % len(arr)]
                if product == -69:
                    result.append(arr[y:z % len(arr) + 1])
    return result