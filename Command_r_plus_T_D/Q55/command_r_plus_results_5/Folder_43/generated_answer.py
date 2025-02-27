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
    sublists = find_product_sublists(circular_list, -26)
    sublists_with_duplicates = []
    for sublist in sublists:
        circular_sublist = sublist + sublist
        for i in range(len(circular_sublist)):
            if circular_sublist[i:i + len(sublist)] == sublist:
                sublists_with_duplicates.append(circular_sublist[i:i + len(sublist)])
    return sublists_with_duplicates