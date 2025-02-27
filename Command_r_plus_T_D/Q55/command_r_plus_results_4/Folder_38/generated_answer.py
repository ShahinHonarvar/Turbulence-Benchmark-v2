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
    all_sublists = []
    for i in range(len(circular_list)):
        circular_sublist = circular_list[i:] + circular_list[:i]
        all_sublists.extend(find_product_sublists(circular_sublist, -23))
    return all_sublists