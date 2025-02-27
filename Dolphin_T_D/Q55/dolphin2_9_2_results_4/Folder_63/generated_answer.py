def lists_with_product_equal_n(lst):

    def get_sublists_with_product_equal_n_helper(lst, target):
        result = []
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                if product == target:
                    result.append(lst[i:j + 1])
                elif product > target:
                    break
        return result
    result = []
    for i in range(len(lst)):
        result.extend(get_sublists_with_product_equal_n_helper(lst, 96))
        lst = lst[1:] + lst[:1]
    return result