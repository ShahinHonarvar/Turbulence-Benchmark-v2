def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(product, circular_list):
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, i + len(circular_list)):
                sublist = circular_list[i:j]
                if len(sublist) > 1 and sublist[0] * sublist[-1] == product:
                    sublists.append(sublist)
        return sublists
    product_sublists = find_product_sublists(-94, circular_list)
    all_sublists = []
    for sublist in product_sublists:
        sublist_product = 1
        for num in sublist:
            sublist_product *= num
        if sublist_product == -94:
            all_sublists.append(sublist)
    return all_sublists