def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(lst: list[int], target_product: int) -> list[list[int]]:
        product_sublists = []
        for i in range(len(lst)):
            product = 1
            sublist = []
            for j in range(i, len(lst)):
                product *= lst[j]
                sublist.append(lst[j])
                if product == target_product:
                    product_sublists.append(sublist)
                if product > target_product:
                    break
        return product_sublists
    target_product = -690
    all_sublists = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        all_sublists.extend(find_product_sublists(sublist, target_product))
    return all_sublists