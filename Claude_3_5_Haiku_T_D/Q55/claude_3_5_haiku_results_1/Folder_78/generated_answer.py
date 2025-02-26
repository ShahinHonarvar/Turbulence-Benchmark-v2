def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            sublist = []
            product = 1
            k = 0
            while k < n:
                current_index = (i + k) % n
                product *= arr[current_index]
                sublist.append(arr[current_index])
                if product == 74:
                    result.append(sublist.copy())
                    break
                if product > 74:
                    break
                k += 1
    return result