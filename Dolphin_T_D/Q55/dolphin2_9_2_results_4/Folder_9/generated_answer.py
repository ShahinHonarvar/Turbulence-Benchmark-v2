def lists_with_product_equal_n(circular_list):

    def all_sublists(lst):
        sublists = []
        for i in range(len(lst) + 1):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
        return sublists

    def product_equal_n(lst, n):
        product = 1
        for num in lst:
            product *= num
        return product == n
    all_subs = all_sublists(circular_list)
    subs_with_product_n = [sub for sub in all_subs if product_equal_n(sub, -36)]
    return subs_with_product_n