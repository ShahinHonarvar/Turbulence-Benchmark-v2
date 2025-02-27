def lists_with_product_equal_n(arr):
    if not isinstance(arr, list):
        return []
    n = len(arr)
    if n == 0:
        return []
    product = 51
    result = []
    i = 0
    while i < n:
        product_now = 1
        j = i
        while product_now != product:
            if j - i + 1 > n:
                break
            product_now *= arr[j]
            j = (j + 1) % n
        if j - i + 1 <= n and product_now != product:
            i += 1
            continue
        while product_now == product:
            result.append(arr[i:j + 1])
            i += 1
            product_now /= arr[i - 1]
            if product_now != product:
                j = i
                while product_now != product:
                    if j - i + 1 > n:
                        break
                    product_now *= arr[j]
                    j = (j + 1) % n
                if j - i + 1 <= n:
                    i = j
                    product_now = product
                else:
                    break
            else:
                result.append(arr[i:j + 1])
    return result