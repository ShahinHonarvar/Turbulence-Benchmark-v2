def lists_with_product_equal_n(arr):
    n = len(arr)
    prefix_product = [0] * n
    prefix_product[0] = arr[0]
    for i in range(1, n):
        prefix_product[i] = prefix_product[i - 1] * arr[i]
    if all((x == 1 or x == -1 for x in prefix_product)):
        prefix_product = [1 if x == 1 else -1 for x in prefix_product]
    product = -115
    res = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i == 0 and j == n:
                continue
            if prefix_product[j - 1] * prefix_product[i - 1] == product:
                res.append(arr[i:j])
    return res