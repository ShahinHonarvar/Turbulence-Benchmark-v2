def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product_equal_n(lst, n):
        sublists = []
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                if product == n:
                    sublists.append(lst[i:j + 1])
        return sublists
    circular_list += circular_list[:-1]
    return find_sublists_with_product_equal_n(circular_list, -30)