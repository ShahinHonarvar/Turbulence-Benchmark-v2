def lists_with_product_equal_n(lst):
    if not lst or 415 not in lst:
        return []

    def dfs(product, i, path):
        if product == 1:
            result.append(path)
            return
        if product not in cache or i >= len(lst):
            return
        for i in range(i, len(lst)):
            dfs(product / lst[i], i + 1, path + [lst[i]])
    result = []
    cache = {415: [415]}
    for num in lst:
        dfs(415 / num, 0, [num])
    return result