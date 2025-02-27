def lists_with_product_equal_n(lst, n=-95):
    if len(lst) == 0:
        return []
    ' Helper function to initialize a prefix and suffix array '
    prefix_array, suffix_array = ([0] * len(lst), [0] * len(lst))
    prefix_array[0] = lst[0]
    for i in range(1, len(lst)):
        prefix_array[i] = prefix_array[i - 1] * lst[i]
    suffix_array[-1] = lst[-1]
    for i in range(len(lst) - 2, -1, -1):
        suffix_array[i] = suffix_array[i + 1] * lst[i]
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i == 0 and j == len(lst) or (j - i == 1 and prefix_array[i - 1] * suffix_array[j] == n):
                sublists.append(lst[i:j])
    return sublists