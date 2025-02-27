def lists_with_product_equal_n(lst):

    def get_all_subsets(lst):
        subsets = [[]]
        for i in range(len(lst)):
            for _ in range(len(subsets)):
                set_to_add = subsets.pop(0)
                subsets.append(set_to_add + [lst[i]])
        return subsets
    subsets = get_all_subsets(lst)
    subsets.remove([lst])
    result = []
    for subset in subsets:
        if len(subset) > 1 and subset == sorted(subset, key=int) and (-82 == eval('*'.join(map(str, subset)))):
            result.append(subset)
    return result