def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(lst: list[int], target_product: int) -> list[list[int]]:
        length = len(lst)
        product_sublists = []
        for i in range(length):
            product = 1
            sublist = []
            for j in range(i, length):
                product *= lst[j]
                sublist.append(lst[j])
                if product == target_product:
                    product_sublists.append(sublist)
        return product_sublists
    product_sublists = find_product_sublists(circular_list, -51)
    circular_product_sublists = []
    for sublist in product_sublists:
        circular_sublist = sublist + sublist[:1]
        circular_product_sublists.append(circular_sublist)
    return circular_product_sublists