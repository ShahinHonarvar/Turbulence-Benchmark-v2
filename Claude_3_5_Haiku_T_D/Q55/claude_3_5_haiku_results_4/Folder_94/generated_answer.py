def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            current_sublist = []
            product = 1
            k = 0
            while k < n:
                current_index = (i + k) % n
                product *= arr[current_index]
                current_sublist.append(arr[current_index])
                if product == -30:
                    result.append(current_sublist.copy())
                if k == j:
                    break
                k += 1
    return result