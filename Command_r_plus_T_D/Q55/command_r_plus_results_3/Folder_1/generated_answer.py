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
                if product > target_product or j == length - 1:
                    break
        return product_sublists
    product_sublists = find_product_sublists(circular_list, -51)
    product_sublists.extend(find_product_sublists(circular_list[::-1], -51))
    unique_sublists = []
    for sublist in product_sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    return unique_sublists