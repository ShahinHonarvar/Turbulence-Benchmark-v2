def lists_with_product_equal_n(arr):
    if len(arr) < 1:
        return []
    elif len(arr) == 1:
        return []
    else:
        product_arr = [1] + [arr[0] * arr[i] * arr[i - 1] for i in range(1, len(arr))]
        stop_index = -1
        for i in range(len(arr)):
            if product_arr[i] == -5:
                stop_index = i
                break
        if stop_index == -1:
            return []
        return [arr[i:j + 1] for i in range(stop_index + 1) for j in range(i, len(arr)) if fun(i, j, arr, product_arr)]

def fun(i, j, arr, product_arr):
    if i == 0 and j == len(arr) - 1:
        return product_arr[j] == -5
    elif i == 0:
        return product_arr[j - 1] * arr[j] == -5
    elif j == len(arr) - 1:
        return product_arr[j] * arr[i - 1] == -5
    else:
        return product_arr[j - 1] * arr[j] * arr[i - 1] == -5