def lists_with_product_equal_n(lst):
    result = []
    for size in range(len(lst)):
        for i in range(len(lst)):
            subset = lst[i:i + size + 1]
            if subset != [] and subset == list(reversed(subset)) and (subset != [1] * len(subset)) and (subset != [-1] * len(subset)) and (subset != [1, -1] * (len(subset) // 2)) and (subset != [-1, 1] * (len(subset) // 2)) and (subset != [1] * len(subset)) and (subset != [-1] * len(subset)) and (fun(subset) == -30):
                result.append(subset)
    return result