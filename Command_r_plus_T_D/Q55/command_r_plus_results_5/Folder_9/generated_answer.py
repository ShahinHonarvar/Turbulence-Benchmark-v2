def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(product, circular_list):
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, i + len(circular_list)):
                sublist = circular_list[i:j]
                if len(sublist) > len(circular_list):
                    break
                if product(sublist) == -36:
                    sublists.append(sublist)
        return sublists
    product_func = lambda x: 1 if not x else x[0] * product_func(x[1:])
    return find_product_sublists(product_func, circular_list)