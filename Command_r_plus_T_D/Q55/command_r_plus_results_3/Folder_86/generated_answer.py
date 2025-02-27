def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(product, circular_list):
        product_sublists = []
        for i in range(len(circular_list)):
            for j in range(i, i + len(circular_list)):
                sublist = circular_list[i:j]
                if len(sublist) > 1 and sublist[0] * sublist[-1] == product:
                    product_sublists.append(sublist)
        return product_sublists
    product_sublists = find_product_sublists(-779, circular_list)
    all_sublists = []
    for sublist in product_sublists:
        for i in range(len(sublist)):
            all_sublists.append(sublist[i:] + sublist[:i])
    return all_sublists