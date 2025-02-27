def lists_with_product_equal_n(lst):
    if not lst:
        return []
    else:
        lst = lst + lst[:1]
        result = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i:j + 1] and np.prod(lst[i:j + 1]) == -20:
                    result.append(lst[i:j + 1])
        return result